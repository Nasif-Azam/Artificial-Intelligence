from ultralytics import YOLO
import cv2
import cvzone
import math

# For WebCam
# capture = cv2.VideoCapture(0) # 0 for single webcam
# capture.set(3,1280) # Prop ID no 3 is for width
# capture.set(4,720) # Prop ID no 4 is for height

# For Videos
capture = cv2.VideoCapture("../Videos/people.mp4")

model = YOLO("../Yolo-weights/yolov8n.pt")  # to create object model

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "potted plant", "bed",
              "dining table", "toilet", "tv monitor", "laptop", "mouse", "remote", "key board", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "tooth brush"
              ]
while True:
    success, img = capture.read()
    results = model(img, stream=True)  # Stream for video

    # Bordered Object in OpenCV
    # for r in results:
    #     boxes = r.boxes
    #     for box in boxes:
    #         x1,y1,x2,y2 = box.xyxy[0] # x and y-axis then x=Width y= Height (box.xywy )
    #         x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # Convert tensor values into Integer
    #         print(x1,y1,x2,y2)
    #         cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,255), 3 ) # Create border by using tensor values, border color, border thickness
    #
    # Bordered Object in CVzone
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]  # x and y-axis then x=Width y= Height (box.xywy )
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert tensor values into Integer
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h), t=5, rt=2, colorR=(255, 0, 255), colorC=(0, 255, 0))  # t=Thickness, rt=Rectangle Thickness, Color of Rectangle, Color of Corner

            # Confidece
            confidence = math.ceil((box.conf[0] * 100)) / 100
            # Classname
            cls = int(box.cls[0])
            cvzone.putTextRect(img, f'{classNames[cls]} {confidence}', (max(0, x1), max(30, y1)), scale=1,
                               thickness=2)  # Classification by label

    cv2.imshow("Image", img)
    cv2.waitKey(1)
