[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cQThrnt4)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15268040&assignment_repo_type=AssignmentRepo)
# INF0429 - Robotics

# Seminário - Navegação Autônoma e Reconhecimento de Sinais de Trânsito Usando Turtlebot4

## Integrantes

Rafael Alves Goiás - 202105865

Matheus Andrade Brandão - 202108784

## Objetivo

O objetivo desse trabalho é criar um protótipo que possa ser usado para melhorar a navegação em veículos autônomos. Vamos trabalhar nessa prototipação, em menor escala, criando um sistema de reconhecimento de sinais de trânsito utilizando o TurtleBot 4.

## Proposta

### Problema:
O problema estudado será a implementação e integração de um sistema de navegação autônoma utilizando o Turtlebot4. O objetivo é explorar a capacidade de mapeamento e navegação com o pacote Nav2, incorporando sensores de câmera e LIDAR para criar um sistema robusto e eficiente capaz de mapear, planejar rotas e navegar autonomamente em um ambiente dinâmico.


### Revisão de Literatura:

- "SLAM for Dummies: A Tutorial Approach to Simultaneous Localization and Mapping" - Este artigo fornece uma introdução compreensiva ao conceito de SLAM, cobrindo tanto os aspectos teóricos quanto práticos.
- "ROS Navigation Stack: Current State and Future Challenges" - Uma revisão detalhada sobre o ROS Navigation Stack, discutindo suas capacidades, limitações e direções futuras.
- "A Comparison of Modern General-Purpose Visual SLAM Approaches" - Este estudo compara diferentes abordagens de SLAM visual, destacando vantagens e desvantagens de cada método.
- "Multi-Sensor Data Fusion for Autonomous Driving: A Survey" - Revisão de técnicas de fusão de dados de múltiplos sensores, essencial para entender como integrar LIDAR e câmera de forma eficaz.
- "Deep Learning for Object Detection and Scene Perception in Autonomous Driving: A Review" - Explora o uso de técnicas de aprendizado profundo para detecção de objetos e percepção de cenas, relevantes para a aplicação de visão computacional no projeto.

### Dataset:
Os dados a serem explorados no projeto incluirão:

- Dados de LIDAR:
Pontos de nuvem 3D coletados pelo sensor LIDAR do Turtlebot4.
Utilizados para construir mapas detalhados do ambiente e detectar obstáculos.

- Dados de Câmera:
Sequências de imagens ou vídeos capturados pela câmera do Turtlebot4.
Utilizados para a criação de mapas visuais, detecção de objetos e auxílio na navegação.

- Dados de Odometria:
Informações de posição e movimento fornecidas pelos sensores de odometria do Turtlebot4.
Utilizados para calcular a posição do robô e corrigir a trajetória.


### Métodos de Visão a Serem Revisados:

- SLAM Visual:

ORB-SLAM: Um dos métodos mais populares de SLAM visual, utilizando recursos de pontos para mapeamento e localização.

VINS-Mono: Algoritmo de SLAM visual-inercial que combina dados visuais e inerciais para melhorar a precisão.

- Detecção e Reconhecimento de Objetos:

YOLO (You Only Look Once): Um método de detecção de objetos em tempo real que pode ser utilizado para identificar obstáculos e características específicas no ambiente.

SSD (Single Shot MultiBox Detector): Outro método eficiente para detecção de objetos em tempo real.

- Fusão de Sensores:

Kalman Filter: Técnica estatística utilizada para combinar dados de múltiplos sensores e melhorar a estimativa da posição e movimento do robô.

Particle Filter: Método probabilístico para fusão de sensores, útil em ambientes complexos e não lineares.

### Avaliação:

- Métricas de Desempenho:

Precisão de Mapeamento: Avaliada comparando o mapa gerado com um mapa de referência do ambiente.

Erro de Localização: Medido pela diferença entre a posição estimada do robô e sua posição real.

Taxa de Sucesso de Navegação: Percentual de rotas completadas com sucesso pelo robô sem colisões.

- Benchmarks:

KITTI Dataset: Conjunto de dados amplamente utilizado para avaliação de sistemas de visão e navegação autônoma, podendo ser usado para validar o desempenho do sistema.

TUM RGB-D Dataset: Outro conjunto de dados comum para avaliar métodos de SLAM visual.

- Testes de Cenário Real:

Testes em Ambientes Controlados: Executar testes de navegação e mapeamento em ambientes controlados para avaliar a robustez do sistema.

Testes em Ambientes Dinâmicos: Avaliar o desempenho do sistema em ambientes dinâmicos com obstáculos móveis e variações de iluminação.
