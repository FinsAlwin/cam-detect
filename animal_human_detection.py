import cv2
from ultralytics import YOLO
import numpy as np

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')  # Nano model for speed

# Open the default camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Define the classes we are interested in
human_class = 0  # 'person' in COCO
animal_classes = {
    15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow',
    20: 'elephant', 21: 'bear', 25: 'bird',
    34: 'tiger', 35: 'leopard', 36: 'monkey', 37: 'snake'
}

def draw_detection(frame, x1, y1, x2, y2, label, color):
    """Helper function to draw bounding boxes and labels"""
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
    cv2.putText(frame, label, (x1, y1 - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

def main():
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Get frame dimensions
        frame_height, frame_width = frame.shape[:2]
        
        # Run detection
        results = model(frame)
        detections = results[0].boxes

        # Process detections
        for box in detections:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])

            # Human detection
            if cls == human_class and conf > 0.5:
                draw_detection(frame, x1, y1, x2, y2, 'Human', (0, 255, 0))

            # Animal detection
            elif cls in animal_classes and conf > 0.5:
                animal_name = animal_classes[cls]
                draw_detection(frame, x1, y1, x2, y2, animal_name.capitalize(), (255, 0, 0))

        # Display frame
        cv2.imshow('Animal & Human Detection', frame)
        
        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 