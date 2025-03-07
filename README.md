# Animal and Human Detection using YOLOv8

This project uses YOLOv8 (You Only Look Once) to detect animals and humans in real-time using a webcam. It is designed to focus on animals commonly found in Kerala, India, such as tigers, leopards, monkeys, and snakes.

## Features

- Real-time detection of humans and animals.
- Bounding boxes with labels for detected objects.
- Customizable list of animals to detect.
- Simple and easy-to-use interface.

## Requirements

- Python 3.11.10
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

```bash
python animal_human_detection.py
```

- Press `q` to quit the application.
- Detected humans will be highlighted in green, and animals will be highlighted in blue.

## Customization

You can modify the `animal_classes` dictionary in `animal_human_detection.py` to add or remove animals based on your needs. For example:

```python
animal_classes = {
    15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow',
    20: 'elephant', 21: 'bear', 25: 'bird',
    34: 'tiger', 35: 'leopard', 36: 'monkey', 37: 'snake'
}
```

## Project Structure

```
animal-human-detection/
├── animal_human_detection.py  # Main detection script
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files to ignore in Git
```

## License

This project is licensed for **educational purposes only**. The code and its derivatives cannot be used for commercial purposes or sold. All rights are reserved by the author.

## Acknowledgments

- [Ultralytics](https://ultralytics.com/) for the YOLOv8 model.
- OpenCV for video processing.
