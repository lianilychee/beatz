import cv2 
import cv
import numpy as np
import time
import pyglet
import pygame


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

	if percent > 0.50:
		return (inst, True)


def stream_video(base_case):
	''' Print matrix of each video frame. '''

	instruments = [
		"snare",
		"hat",
		"tom",
		"bass"
	]

	# Initialize sounds
	sounds = [pyglet.resource.media('audio/' + instr + '.ogg', streaming=False) for instr in instruments]

	playing = [False] * len(sounds)
	positions = [
		(37,180, 80,150),
		(37,180, 380,450),
		(467,610, 80,150),
		(467,610, 380,450)
	]


	prev = base_case

	# print len(prev)

	while(cap.isOpened()):
		ret, frame = cap.read()

		area = 143*70

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Check presence of instruments, play sounds
		for i, sound in enumerate(sounds):
			if not playing[i] and check_presence(prev, gray, area, instruments[i], *positions[i]):
				playing[i] = True
				sound.play()
				break
			else:
				playing[i] = False

	
		cv2.rectangle(gray, (37,80), (180,150), (128,114,250), -1) # Snare
		cv2.rectangle(gray, (37,380), (180,450), (204,50,153), -1) # Tom
		cv2.rectangle(gray, (467,80), (610,150), (250,128,114), -1) # Hat
		cv2.rectangle(gray, (467,380), (610,450), (127,255,0), -1) # Bass

		
		cv2.imshow('frame', gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			cap.release()
			cv2.destroyAllWindows()


if __name__ == '__main__':
	# Initialize the camera.

	# pygame.init()
	# pygame.mixer.music.load('audio/bass.ogg')
	# pygame.mixer.music.play()
	# print 'bass'
	# time.sleep(1)
	# pygame.mixer.music.load('audio/tom.ogg')
	# pygame.mixer.music.play()
	# print 'tom'

	instruments = [
		"snare",
		"hat",
		"tom",
		"bass"
	]

	# # Initialize sounds
	# sounds = [pyglet.resource.media('audio/' + instr + '.ogg', streaming=False) for instr in instruments]
	sound = pyglet.resource.media('audio/snare.ogg', streaming=False)
	sound.play()

	# sounds[0].play()

	# cap = cv2.VideoCapture(0)
	# base_case = get_base_case()
	# stream_video( base_case )