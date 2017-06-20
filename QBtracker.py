# Author: Adolfo Moreno

# Import needed libraries
import numpy as np
import cv2
import imutils

# Load our video located in our root folder.
cap = cv2.VideoCapture('IMG_3738.mov')

# iterate through the video frame by frame.
while(1):
    # read our first frame
    frame = cap.read()
    # reduce frame size so that we can better see the changes
    frame = imutils.resize(frame, width=600)
    # First method track using color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # We want to only track red in this example because qb is wearing all red.
    # Thus we selected our range for the color red.
    lower_red = np.array([150,150,50])
    upper_red = np.array([255,255,180])

    # Create a mask with our hue values to single out color.
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # Erode our image to reduce noise level and single out our color.
    mask = cv2.erode(mask, None, iterations = 2)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # show the frame
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# finish up by closing the preview windows and reseting.
cv2.destroyAllWindows()
cap.release()
