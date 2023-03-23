import cv2
import numpy as np
# Print the version of OpenCV



# Wait for any key to be pressed
img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("Image", img)
# Define a variable for radius
R = 10
while True:
    # 0 means wait for any key to be pressed
    # 1 means wait for 1 millisecond
    k = cv2.waitKey(0) 
    if k==ord('+'):
        R += 1
    elif k==ord('-'):
        R -= 1


    
    
    # Draw a circle to the center of the image
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.circle(img, (256, 256), R, (0, 0, 255), 2)
    
    cv2.imshow("Image", img)
    
    if k == 27:
        break

# Close all windows
cv2.destroyAllWindows()