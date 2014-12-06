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

	ramp_frames = 10  # get multiple temporary images to allow camera to adjust to environment.

	for i in xrange(ramp_frames):
		temp = get_image()

	camera_capture = cv.cvtColor(get_image(), cv.COLOR_BGR2GRAY)

	cv.imwrite("/home/baseCase.jpg", camera_capture)
	del(camera) # close camera port.

	time.sleep(3) # delay to allow user to acclimate

	print 'Base case CAPTURED.'

	return camera_capture


def get_difference(prev, current, lowerX, upperX):
	''' Gets the difference between baseCase.jpg each video frame. '''

	diff = cv.absdiff(prev, current)

	# diff[ ymin:ymax , xmin:xmax]
	trueCount = len( np.where(diff[0:480 , lowerX:upperX]>20)[0] )

	return trueCount 


def check_presence(trueCount):
	''' Within a bounded region, check if an object has appeared. '''

	area = 213*480
	percent = trueCount / area

	if percent > 0:
		print true


def stream_video(base_case):
	''' Print matrix of each video frame. '''

	prev = base_case

	while(camera.isOpened()):
		ret, frame = camera.read()

		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		trueCount = get_difference(prev, gray, 0, 210)

		print trueCount

		cv.imshow('frame', gray)
		if cv.waitKey(1) & 0xFF == ord('q'):

	cap.release()
	cv.destroyAllWindows()


if __name__ == '__main__':
	base_case = get_base_case()
	stream_video( base_case )