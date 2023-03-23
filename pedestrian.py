import cv2
import numpy as np
# Print the version of OpenCV



# Wait for any key to be pressed
img = cv2.imread("pedestrian_crossing.jpg")
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img)
upper = 0
lower = 10
while True:
    # 0 means wait for any key to be pressed
    # 1 means wait for 1 millisecond
    cv2.imshow("Image", img)
    cv2.imshow("Gray", gray)
    mask = cv2.inRange(gray,
                        lower, 
                        upper)
    k = cv2.waitKey(1)
    if k==ord('+'):
        upper += 1
    elif k==ord('-'):
        lower -= 1

    cv2.imshow("Mask", mask)
    if k == 27:
        break


cv2.destroyAllWindows()



    