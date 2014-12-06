import cv2 as cv
import numpy as np
import time

camera_port = 0
ramp_frames = 30
camera = cv.VideoCapture(camera_port)

def get_image():
	retval, im = camera.read()
	return im

for i in xrange(ramp_frames):
	temp = get_image()
print "Taking image..."

camera_capture = get_image()
file = "/home/liani/Documents/beatz/testimage.jpg"
cv.imwrite(file, camera_capture)
del(camera)



# # CAPTURING THE BASE CASE
# cv.NamedWindow("camera",1)
# capture = cv.CaptureFromCAM(0)
# while True:
# 	img = cv.QueryFrame(capture)
# 	cv.ShowImage("camera",img)
# 	base = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 	cv.SaveImage("baseCase.jpg",base)
# 	if cv.WaitKey(10) == 27:
# 		break

# img = cv.QueryFrame(capture)
# img.imshow()

# cap = cv.VideoCapture('motionTrackingTutorial/bouncingBall.avi')
cap = cv.VideoCapture(capture)

count = 0
a = []

while(cap.isOpened()):
	ret, frame = cap.read()

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	a.append = np.asarray(gray)
	time.sleep(1)
	print a[count]

	cv.imshow('frame', gray)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

	count = count + 1


cap.release()
cv.destroyAllWindows()


