import cv2 as cv
import numpy as np
import time

# cap = cv.VideoCapture('motionTrackingTutorial/bouncingBall.avi')
cap = cv.VideoCapture(0)


while(cap.isOpened()):
	ret, frame = cap.read()

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	cv.imshow('frame', frame)

	a = np.asarray(gray)
	time.sleep(1)

	print a


	cv.imshow('frame', gray)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
cv.destroyAllWindows()


