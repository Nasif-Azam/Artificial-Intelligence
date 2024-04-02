from ultralytics import YOLO
import cv2
import cvzone
import math
import PokerHandFunction

# For WebCam
capture = cv2.VideoCapture(1)  # 0 for single webcam
capture.set(3, 1280)  # Prop ID no 3 is for width
capture.set(4, 720)  # Prop ID no 4 is for height

# For Videos
# capture = cv2.VideoCapture("../Videos/people.mp4")

model = YOLO("playingCards.pt")  # to create object model
classNames = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']

while True:
    success, img = capture.read()
    results = model(img, stream=True)  # Stream for video
    hand = []
    # Bordered Object in CVzone
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]  # x and y-axis then x=Width y= Height (box.xywy )
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert tensor values into Integer
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            # cvzone.cornerRect(img, (x1, y1, w, h), t=5, rt=2, colorR=(255, 0, 255), colorC=(
            #         0, 255, 0))  # t=Thickness, rt=Rectangle Thickness, Color of Rectangle, Color of Corner

            # Confidece
            confidence = math.ceil((box.conf[0] * 100)) / 100
            # Classname
            cls = int(box.cls[0])
            currentClass = classNames[cls]
            cvzone.putTextRect(img, f'{currentClass} {int(confidence * 100)}%', (max(0, x1), max(35, y1)), scale=1,
                               thickness=2)  # Classification by label

            if confidence > 0.5:
                hand.append(currentClass)

    # print(hand)
    hand = list(set(hand))
    # print(hand)
    if len(hand) == 5:
        results = PokerHandFunction.findPokerHand(hand)
        print(results)
    cvzone.putTextRect(img, f'Your Hand: {results}', (50, 50), scale=3, thickness=5)  # Classification by label

    cv2.imshow("Image", img)
    cv2.waitKey(1)
