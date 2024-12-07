from ultralytics import YOLO
import cv2
import numpy as np
from window_capture import WindowCapture

wincap = WindowCapture()
model = YOLO("weights/nano_best.pt")  # Path to your YOLO model

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1920, 1080))

# Set the duration for capturing video (2 minutes)
duration = 2 * 60  # 2 minutes in seconds
start_time = cv2.getTickCount()

def get_bounding_boxes(results):
    boxes = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = [round(coord, 2) for coord in box.xyxy[0].tolist()]
            class_id = int(box.cls[0])
            class_name = result.names[class_id]
            boxes.append((x1, y1, x2, y2, class_name))
    return boxes

# Loop for continuous detection
while True:
    screenshot = wincap.get_screenshot()
    results = model.predict(source=screenshot, save=False, show=False)
    annotated_frame = results[0].plot()
    print(get_bounding_boxes(results))

    # out.write(annotated_frame)
    cv2.imshow("YOLO Detection", annotated_frame)
    cv2.waitKey()
    # Break the loop if 'q' is pressed or duration is exceeded
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # if (cv2.getTickCount() - start_time) / cv2.getTickFrequency() > duration:
    #     break

# Release resources
out.release()
cv2.destroyAllWindows()

