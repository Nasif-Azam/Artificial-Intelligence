from ultralytics import YOLO
import cv2
import cvzone
import math

# For WebCam
# capture = cv2.VideoCapture(0) # 0 for single webcam
# capture.set(3,1280) # Prop ID no 3 is for width
# capture.set(4,720) # Prop ID no 4 is for height

# For Videos
capture = cv2.VideoCapture("../Videos/ppe-1.mp4")

model = YOLO("ppe.pt")  # to create object model

classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest',
              'machinery', 'vehicle']
# myColor = (0, 0, 255)

while True:
    success, img = capture.read()
    results = model(img, stream=True)  # Stream for video

    # Bordered Object in CVzone
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]  # x and y-axis then x=Width y= Height (box.xywy )
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert tensor values into Integer
            w, h = x2 - x1, y2 - y1

            # cvzone.cornerRect(img, (x1, y1, w, h), t=5, rt=2, colorR=(255, 0, 255), colorC=(0, 255, 0))  # t=Thickness, rt=Rectangle Thickness, Color of Rectangle, Color of Corner

            # Confidece
            confidence = math.ceil((box.conf[0] * 100)) / 100
            # Classname
            cls = int(box.cls[0])
            currentClass = classNames[cls]
            if confidence > 0.5:
                if currentClass == 'Hardhat' or currentClass == 'Mask' or currentClass == 'Safety Cone' or currentClass == 'Safety Vest' :
                    myColor = (0, 255, 0)
                elif currentClass == 'NO-Hardhat' or currentClass == 'NO-Mask' or currentClass == 'NO-Safety Vest' :
                    myColor = (0, 0, 255)
                else:
                    myColor = (255, 0, 0)

                cvzone.putTextRect(img, f'{currentClass} {confidence}', (max(0, x1), max(30, y1)), scale=1.5, offset=5,
                                   thickness=2, colorB=myColor, colorT=(255, 255, 255), colorR=myColor)  # Classification by label
                cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 2)  # Thickness=3

    cv2.imshow("Image", img)
    cv2.waitKey(1)
