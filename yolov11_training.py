from ultralytics import YOLO

# Load a model
model = YOLO("yolo11s.pt")

# Train the model
train_results = model.train(
    data="dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=32,  
    device="cpu",
    name="hollow_knight_experiment"
)

# Evaluate model performance on the validation set
metrics = model.val()