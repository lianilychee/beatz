import cv2 
import cv
import numpy as np
import time


def get_image():
	''' Retrieve single frame from camera. '''
	retval, im = cap.read()
	return im


def get_base_case():
	''' Retrieve base case image for subsequent video frames to compare against. '''

	print 'Capturing base case image.'

	cap = cv2.VideoCapture(0)

	ramp_frames = 10  # get multiple temporary images to allow camera to adjust to environment.

	for i in xrange(ramp_frames):
		temp = get_image()

	camera_capture = cv2.cvtColor(get_image(), cv2.COLOR_BGR2GRAY)

	cv2.imwrite("baseCase.jpg", camera_capture)
	del(cap) # close camera port.

	time.sleep(3) # delay to allow user to acclimate

	print 'Base case CAPTURED.'

	return camera_capture


def check_presence(prev, current, area, inst, lowerX, upperX, lowerY, upperY):
	''' Within a bounded region, check if an object has appeared. '''

	diff = cv2.absdiff(prev, current)
	# diffT = zip(*diff)	

	# trueCount is the number of pixels within a region that have changed from the base case.
	trueCount = len( np.where(diff[lowerY:upperY,lowerX:upperX] > 20)[0] )

	percent = trueCount / float(area)

	print percent

	if percent > 0.50:
		print inst


def stream_video(base_case):
	''' Print matrix of each video frame. '''

	prev = base_case

	print len(prev)


	while(cap.isOpened()):
		ret, frame = cap.read()

		area = 143*70

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Check presence of snare
		check_presence(prev, gray, area, 'snare', 37,180, 80,150)

		# Check presence of tom
		check_presence(prev, gray, area, 'tom', 37,180, 380,450)

		# Check presence of hat
		check_presence(prev, gray, area, 'hat', 467,610, 80,150)

		# Check presence of bass
		check_presence(prev, gray, area, 'bass', 467,610, 380,450)

		### Draw the snare rectangle for testing

		cv2.rectangle(gray, (37,80), (180,150), (128,114,250), -1) # Snare
		cv2.rectangle(gray, (37,380), (180,450), (204,50,153), -1) # Tom
		cv2.rectangle(gray, (467,80), (610,150), (250,128,114), -1) # Hat
		cv2.rectangle(gray, (467,380), (610,450), (127,255,0), -1) # Bass



		# flipped = cv.Flip(gray, flipMode = 0)
		
		cv2.imshow('frame', gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			cap.release()
			cv2.destroyAllWindows()


if __name__ == '__main__':
	# Initialize the camera.
	cap = cv2.VideoCapture(0)
	base_case = get_base_case()
	stream_video( base_case )
