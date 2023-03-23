import cv2
import numpy as np
# Print the version of OpenCV
print(cv2.__version__)

img = np.zeros((512, 512, 3), np.uint8)
# Draw a circle to the center of the image
cv2.circle(img, (256, 256), 100, (0, 0, 255), 2)
cv2.imshow("Image", img)
# Wait for any key to be pressed
while True:
    # 0 means wait for any key to be pressed
    # 1 means wait for 1 millisecond
    k = cv2.waitKey(0) 
    print(k)
    if k == 27:
        break

# Close all windows
cv2.destroyAllWindows()