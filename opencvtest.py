import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

	# Take each frame
	_, frame = cap.read()

	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Define filter thresholds
	# lower_red = np.array([159,50,50])
	lower_red = np.array([0,94,66])
	upper_red = np.array([179,255,255])
	# upper_red = np.array([0,100,100])

	# lower_blue = np.array([110,50,50])
	# upper_blue = np.array([130,255,255])

	# mask = cv2.inRange(hsv, lower_blue, upper_blue)
	mask = cv2.inRange(hsv, lower_red, upper_red)

	res = cv2.bitwise_and(frame,frame, mask=mask)

	cv2.imshow('frame',frame)
	# cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()