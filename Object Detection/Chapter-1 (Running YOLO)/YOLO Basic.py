from ultralytics import  YOLO
import cv2

# model = YOLO('../Yolo-Weights/yolov8l.pt') # l for large YOLO version more object
model = YOLO('../Yolo-Weights/yolov8n.pt') # n for nano YOLO version less object

# result = model("Image/cars.jpg", show=True)
result = model("Image/peopleSchoolBus.jpg", show=True)
cv2.waitKey(0)
