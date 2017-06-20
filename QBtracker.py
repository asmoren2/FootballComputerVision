# Author: Adolfo Moreno

# Import needed libraries
import numpy as np
import cv2
import imutils

# Load our video located in our root folder.
cap = cv2.VideoCapture('IMG_3738.mov')

# iterate through the video frame by frame.
while(1):
    frame = cap.read()
    # show the frame
    cv2.imshow('frame',frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# finish up by closing the preview windows and reseting.
cv2.destroyAllWindows()
cap.release()
