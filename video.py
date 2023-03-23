import cv2
import numpy as np

# Read the video from file
cap = cv2.VideoCapture("video.mp4")
ret, frame = cap.read()
print(ret)