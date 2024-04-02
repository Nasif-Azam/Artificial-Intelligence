from ultralytics import YOLO
import cv2
import cvzone
import math
import TeenPattiFunction

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
resultArray = []  # Create an empty array

TeenPattiFunction.findTeenPattiHand()

# while True:
#     hand = []
#     if len(hand) == 3:
#         results = TeenPattiFunction.findTeenPattiHand(hand)
#         if results == "Trio(3 of a Kind)":
#             resultArray.append({6})
#         elif results == "Pure Sequence(Straight Flush)":
#             resultArray.append({5})
#         elif results == "Sequence(Straight)":
#             resultArray.append({4})
#         elif results == "Color(Flush)":
#             resultArray.append({3})
#         elif results == "Pair":
#             resultArray.append({2})
#         else:
#             resultArray.append({1})
#
#
#     print(resultArray)
#     # Find common elements
#     if len(resultArray) > 1:
#         commonElements = set(resultArray[0]).intersection(*resultArray[1:])
#         highestCommonElement = max(commonElements)
#         print("Common Elements:", commonElements)
#         print("Highest Common Element:", highestCommonElement)
