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
	''' Retrieve base case image for subsequent video frames to compare against. '''

	print 'Capturing base case image.'

	camera = cv.VideoCapture(0)

	ramp_frames = 10  # Capture multiple temporary images to allow camera to adjust to environment.

	for i in xrange(ramp_frames):
		temp = get_image()

	# camera_capture = get_image()
	camera_capture = cv.cvtColor(get_image(), cv.COLOR_BGR2GRAY)

	cv.imwrite("/home/liani/Documents/beatz/baseCase.jpg", camera_capture)
	del(camera) # close the camera port.

	time.sleep(5)

	print 'Base case CAPTURED.'

	return camera_capture


def stream_video(base_case):
	''' Print matrix of each video frame. '''

	prev = base_case

	# cap = cv.VideoCapture(0)

	# ### GRAB VERY FIRST FRAME
	# ret, frame = camera.read()
	# prev = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	while(camera.isOpened()):
		ret, frame = camera.read()

		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		get_difference(prev, gray, 0, 210)

		cv.imshow('frame', gray)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break

		# # Overwrites previous frame
		# prev = gray

	cap.release()
	cv.destroyAllWindows()


def get_difference(prev, current, lowerX, upperX):
	''' Gets the difference between baseCase.jpg and testCase.jpg. '''

	diff = cv.absdiff(prev, current)

	trueCount = len( np.where(diff[lowerX:upperX, 0:480]>20)[0] )
	print trueCount
	# 	print len(np.where(diff > 50)[0])

	# [height,width,depth] = diff.shape

	# return [height,width]

	return diff


if __name__ == '__main__':
	# get_base_case()
	stream_video( get_base_case() )
	# print get_difference()