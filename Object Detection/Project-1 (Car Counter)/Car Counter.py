import numpy as np
from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *

# For Videos
capture = cv2.VideoCapture("../Videos/cars3.mp4")  # to access video file

model = YOLO("../Yolo-Weights/yolov8l.pt")  # to create object model

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
mask = cv2.imread("Image/mask.png") # Masking image for video capture
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3) # Instance of sort
# Line drawing Limits
limits = [20, 300, 570, 300] # X, X', Y, Y'
# pt1 = (0,0)
# pt2 = (100,100)
totalCount = []
while True:
    success, img = capture.read()
    imgRegion = cv2.bitwise_and(img, mask) # Overlay the mask into the image

    imgGraphics = cv2.imread("Image/graphics.png", cv2.IMREAD_UNCHANGED)
    img = cvzone.overlayPNG(img, imgGraphics, (0, 0))
    results = model(imgRegion, stream=True)  # Stream for video mask generation

    detections = np.empty((0, 5)) # Detection array with numpy

    # Bordered Object in CVzone
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]  # x and y-axis then x=Width y= Height (box.xywy )
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert tensor values into Integer
            w, h = x2 - x1, y2 - y1 # Calculate the perfect width & height

            # Confidece
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Classname
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if currentClass == "car" or currentClass == "truck" or currentClass == "bus" \
                    or currentClass == "motorbike" and conf > 0.3:
                # cvzone.putTextRect(img, f'{currentClass} {confidence}', (max(0, x1), max(30, y1)), scale=1, thickness=2,
                #                    offset=5)  # Classification by label
                # cvzone.cornerRect(img, (x1, y1, w, h), t=5, rt=5, colorR=(255, 0, 255), colorC=(
                #     0, 255, 0), l=9)  # t=Thickness, rt=Rectangle Thickness, Color of Rectangle, Color of Corner
                currentArray = np.array([x1, y1, x2, y2, conf]) # Initial numpy array
                detections = np.vstack((detections, currentArray)) # Appending detections and currentArray to directions instead of using .append

    resultsTracker = tracker.update(detections)

    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 255), 5) # Color Red and Thickness 5
    for result in resultsTracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 255))
        cvzone.putTextRect(img, f' {int(id)}', (max(0, x1), max(35, y1)),
                           scale=2, thickness=3, offset=10)

        cx, cy = x1 + w // 2, y1 + h // 2
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        if limits[0] < cx < limits[2] and limits[1] - 15 < cy < limits[1] + 15:
            if totalCount.count(id) == 0:
                totalCount.append(id)
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 5)

    # cvzone.putTextRect(img, f' Count: {totalCount}', (50, 50))
    cv2.putText(img, str(len(totalCount)), (255, 100), cv2.FONT_HERSHEY_PLAIN, 5, (50, 50, 255), 8)

    cv2.imshow("Image", img)
    # cv2.imshow("ImageRegion", imgRegion)
    cv2.waitKey(0)
