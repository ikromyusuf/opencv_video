import cv2
import numpy as np

# Read the video from file
cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()