import cv2 as cv
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

	# Video capture
	_, frame = cap.read()
		# NOTE: default frame size: 639 by 478

	cv.AbsDiff()

	# Convert BGR to HSV
	hsv = cv.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Define filter thresholds
	lower_red = np.array([50,40,40])
	upper_red = np.array([179,255,255])

	# mask = cv2.inRange(hsv, lower_blue, upper_blue)
	mask = cv.inRange(hsv, lower_red, upper_red)

	res = cv.bitwise_and(frame,frame, mask=mask)

	cv.imshow('frame',frame) # live stream
	# cv2.imshow('res',res) # pulling out red
	# cv2.imshow('mask',mask) # black and white only
	k = cv.waitKey(5) & 0xFF
	if k == 27:
		break

cv.destroyAllWindows()