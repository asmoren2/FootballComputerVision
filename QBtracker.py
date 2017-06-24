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
    ret, frame = cap.read()
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
    # Erode and dialate our image to reduce noise level and single out our color.
    mask = cv2.erode(mask, None, iterations = 2)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # create our contours so that we can draw our rectangle that follows QB
    _,contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0 # hold our maximum contour area
    best_contour = None # hold the biggest contour in our frame

    # Find the biggest contour which will avoid small discrepancies and will be QB
    for c in contours:
        currentArea = cv2.contourArea(c)
        if currentArea > max_area:
            best_contour = c
            max_area = currentArea
    if best_contour is not None:
        # Get our coordinates and draw rectangle on frame
        x,y,w,h = cv2.boundingRect(best_contour)
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,0,255), 3)


    # show the frame
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# finish up by closing the preview windows and reseting.
cv2.destroyAllWindows()
cap.release()
