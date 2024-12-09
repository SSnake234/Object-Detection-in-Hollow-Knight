from ultralytics import YOLO

# Load a model, n for Nano and s for Small (there are also Medium and Large models)
model = YOLO("yolo11s.pt")

# Train the model
train_results = model.train(
    data="grimm_dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=32,  
    device="cpu", # Change to "0" for GPU
)

metrics = model.val()