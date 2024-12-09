from ultralytics import YOLO
import cv2 as cv
import numpy as np
from window_capture import WindowCapture

wincap = WindowCapture()
model = YOLO("grimm_results/nano/train/weights/best.pt")  # Path to your YOLO model

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('demo_videos/grimm_nano_demo.avi', fourcc, 10.0, (1920, 1080))

# Set the duration for capturing video
duration = 1.5 * 60  
start_time = cv.getTickCount()

def get_bounding_boxes(results):
    boxes = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = [round(coord, 2) for coord in box.xyxy[0].tolist()]
            class_id = int(box.cls[0])
            class_name = result.names[class_id]
            boxes.append((x1, y1, x2, y2, class_name))
    return boxes

# Capture video
while True:
    screenshot = wincap.get_screenshot()
    results = model.predict(source=screenshot, save=False, show=False)
    annotated_frame = results[0].plot() 
    # print(get_bounding_boxes(results))

    out.write(annotated_frame)
    # cv.imshow("YOLO Detection", annotated_frame)
    
    # Break the loop if 'q' is pressed or duration is exceeded
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if (cv.getTickCount() - start_time) / cv.getTickFrequency() > duration:
        break

# Release resources
out.release()
cv.destroyAllWindows()

