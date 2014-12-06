import cv2 as cv
import numpy as np
import time


# Initialize the camera.
camera = cv.VideoCapture(0)


def get_image():
	''' Retrieve single frame from camera. '''
	retval, im = camera.read()
	return im


def get_base_case():
	''' Retrieve base case image for subsequent video capture frames to compare against. '''

	camera = cv.VideoCapture(0)

	ramp_frames = 10  # Capture multiple temporary images to allow camera to adjust to environment.

	for i in xrange(ramp_frames):
		temp = get_image()
	print "Capturing base case image."

	# camera_capture = get_image()
	camera_capture = cv.cvtColor(get_image(), cv.COLOR_BGR2GRAY)

	cv.imwrite("/home/liani/Documents/beatz/baseCase.jpg", camera_capture)
	del(camera) # close the camera port.


def stream_video():
	''' Print matrix of each video frame. '''

	# cap = cv.VideoCapture('motionTrackingTutorial/bouncingBall.avi')
	cap = cv.VideoCapture(0)

	count = 0
	a = []

	while(camera.isOpened()):
		ret, frame = camera.read()

		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		# a.append = np.asarray(gray)
		a = np.asarray(gray)
		time.sleep(1)
		print a[count]

		cv.imshow('frame', gray)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break

		count = count + 1


	cap.release()
	cv.destroyAllWindows()


get_base_case()
# stream_video()