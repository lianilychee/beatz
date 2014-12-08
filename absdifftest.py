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

	cv.imwrite("baseCase.jpg", camera_capture)
	del(camera) # close camera port.

	time.sleep(3) # delay to allow user to acclimate

	print 'Base case CAPTURED.'

	return camera_capture


def check_presence(prev, current, lowerX, upperX, lowerY, upperY):
	''' Within a bounded region, check if an object has appeared. '''

	diff = cv.absdiff(prev, current)
	diffT = zip(*diff)	

	# trueCount is the number of pixels within a region that have changed from the base case.
	# trueCount = len( np.where(diff[0:480, lowerX:upperX]>0)[0] )
	# trueCount = len( np.where(diff[0:240][0:320]>100)[0] )

	# Checking within a horizontal band.
	trueCountHoriz = len( np.where(diff[lowerY:upperY]>100)[0] )
	trueCountVert = len( np.where(diffT[lowerX:upperX]>100)[1] )
	# count = np.where(diff[lowerY:upperY]>100)[0]

	# print trueCount

	# Calculate the area of region of interest (ROI)..
	# area = abs(lowerX-upperX) * abs(lowerY-upperY)
	area = 640*480

	# Calculate the percentage of pixels chanegd within ROI.
	# percent = trueCount / area

	return trueCountVert

	# print percent

	# if percent > 0:
	# 	print 'YES'
	# else:
	# 	print 'NOT YET'


def stream_video(base_case):
	''' Print matrix of each video frame. '''

	prev = base_case

	print len(prev)


	while(camera.isOpened()):
		ret, frame = camera.read()

		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		# Draw the snare rectangle for testing
		BLACK = (0, 0, 0)
		font = cv.FONT_HERSHEY_SIMPLEX
		cv.rectangle(gray, (37,80), (180,150), (128,114,250), -1) # Snare
		cv.putText(gray, 'SNARE', (50,130), font, 1, BLACK, 2, 5)


		# Check presence of snare and hihat
		print check_presence(prev, gray, 37,180, 80,150)

		# print trueCount = get_difference(prev, gray, 37,180, 80,150 )

		cv.imshow('frame', gray)
		if cv.waitKey(1) & 0xFF == ord('q'):
			camera.release()
			cv.destroyAllWindows()


if __name__ == '__main__':
	base_case = get_base_case()
	stream_video( base_case )