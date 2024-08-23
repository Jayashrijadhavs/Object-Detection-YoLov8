import cv2
import json
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

def process_video(video_path, model):
    results = []
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        
        # Detect objects
        detections = model(frame)

        # Process each detection
        for det in detections[0].boxes:
            x_min, y_min, x_max, y_max = det.xyxy[0].tolist()  # Convert tensor to list
            confidence = det.conf[0].item()  # Convert single-element tensor to float
            class_name = det.cls[0].item()  # Convert single-element tensor to int

            results.append({
                'frame': frame_count,
                'class': class_name,
                'confidence': confidence,
                'x_min': x_min,
                'y_min': y_min,
                'x_max': x_max,
                'y_max': y_max
            })
    
    cap.release()
    return results

def generate_copywriting(detected_objects):
    num_objects = len(detected_objects)
    copywriting = f"Just captured a video with {num_objects} objects detected! Stay tuned for more updates."
    return copywriting
copywriting = generate_copywriting(detected_objects)
copywriting