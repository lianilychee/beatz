import cv2
import cv2.cv as cv
import numpy as np
import time

# Okay, I shouldn't have to use the cv2.cv package.  I should just be able to use cv2 and call it a day.  


# CAPTURING THE BASE CASE
cv.NamedWindow("camera",1)
capture = cv.CaptureFromCAM(0)
while True:
	img = cv.QueryFrame(capture)
	cv.ShowImage("camera",img)
	base = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv.SaveImage("baseCase.jpg",base)
	if cv.WaitKey(10) == 27:
		break

img = cv.QueryFrame(capture)
img.imshow()

# cap = cv.VideoCapture('motionTrackingTutorial/bouncingBall.avi')
cap = cv2.VideoCapture(capture)

count = 0
a = []

while(cap.isOpened()):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	a.append = np.asarray(gray)
	time.sleep(1)
	print a[count]

	cv.imshow('frame', gray)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

	count = count + 1


cap.release()
cv2.destroyAllWindows()


