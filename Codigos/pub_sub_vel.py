import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import torch

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(Image, '/oakd/rgb/preview/image_raw', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()

        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp3/weights/best.pt', force_reload=True)

        self.vel_subscription = self.create_subscription(Twist, '/cmd_vel', self.vel_callback, 10)
        self.vel_publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        self.current_velocity = Twist()

    def vel_callback(self, msg):
        self.current_velocity = msg

    def listener_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        results = self.model(cv_image)

        detected_stop = False
        detected_speedlimit = False

        for pred in results.xyxy[0].cpu().numpy():
            x1, y1, x2, y2, conf, cls = pred
            label = f"{self.model.names[int(cls)]} {conf:.2f}"

            if self.model.names[int(cls)] == "stop":
                detected_stop = True
            
            if self.model.names[int(cls)] == "speedlimit":
                detected_speedlimit = True

            cv2.rectangle(cv_image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(cv_image, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        if detected_stop:
            new_velocity = Twist()
            self.vel_publisher.publish(new_velocity)
        elif detected_speedlimit:
            new_velocity = Twist()
            new_velocity.linear.x = self.current_velocity.linear.x * 0.5
            new_velocity.angular.z = self.current_velocity.angular.z
            self.vel_publisher.publish(new_velocity)
        else:
            self.vel_publisher.publish(self.current_velocity)

        cv2.imshow('YOLOv5 Inference', cv_image)
        cv2.waitKey(1)

        print(f"STOP: {detected_stop}")
        print(f"Speed Limit: {detected_speedlimit}")

def main(args=None):
    rclpy.init(args=args)

    image_subscriber = ImageSubscriber()

    try:
        rclpy.spin(image_subscriber)
    except KeyboardInterrupt:
        pass

    cv2.destroyAllWindows()
    image_subscriber.destroy_node()
    rclpy.shutdown()
    print('finish')

if __name__ == '__main__':
    main()
