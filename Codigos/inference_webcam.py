import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp3/weights/best.pt', force_reload=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao abrir a webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Falha na captura do frame")
        break

    results = model(frame)

    detected_stop = False

    for pred in results.xyxy[0].cpu().numpy():
        x1, y1, x2, y2, conf, cls = pred
        label = f"{model.names[int(cls)]} {conf:.2f}"
        
        if model.names[int(cls)] == "stop":
            detected_stop = True

        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('YOLOv5 Inference', frame)

    print(f"Detected stop: {detected_stop}")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


