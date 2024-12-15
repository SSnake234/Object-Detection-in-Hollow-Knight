# Object Detection in Hollow Knight

This is a personal project of mine to get accustomed to OpenCV and YOLO model.

## Run code

### OpenCV Object Detection
To run the OpenCV object detection:
1. Run the `main.py` script.
   - The Knight will jump when facing left and hit when facing right.

### YOLO Object Detection
To run YOLO object detection:
1. Run the `inference.py` script.
   - The resulting videos will be stored in the folder `demo_videos`.

## Datasets
I have trained the YOLO model for two bosses:
- **Hornet**
  - The dataset was taken from [this dataset on Roboflow](https://universe.roboflow.com/ia2024-fxgam/hollow-knight-ea49k/dataset/9).
- **Troupe Master Grimm**
  - I created this dataset using Roboflow, and you can find it [here](https://universe.roboflow.com/image-annotation-xskos/hollow-knight-vs-grimm/dataset/3).

## Model
The YOLO models I trained were YOLOv11 nano and small for each dataset. The demo videos were generated using the nano model for each boss.
