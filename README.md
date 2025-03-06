# Animal and Human Detection using YOLOv8

This project uses YOLOv8 (You Only Look Once) to detect animals and humans in real-time using a webcam. It is designed to focus on animals commonly found in Kerala, India, such as tigers, leopards, monkeys, and snakes.

## Features

- Real-time detection of humans and animals.
- Bounding boxes with labels for detected objects.
- Customizable list of animals to detect.
- Simple and easy-to-use interface.

## Requirements

- Python 3.7 or higher
- OpenCV
- Ultralytics (YOLOv8)
- NumPy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/animal-human-detection.git
   cd animal-human-detection
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the YOLOv8 model weights (if not already included):
   ```bash
   wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
   ```

## Usage

Run the detection script:
