import cv2 
import cv
import numpy as np
import time
import pygame
from pydub import AudioSegment

def get_image():
    ''' Retrieve single frame from camera. '''
    retval, im = cap.read()
    return im



def get_base_case(cap):
    ''' Retrieve base case image for subsequent video frames to compare against. '''

    print 'Capturing base case image.'

    ramp_frames = 10  # get multiple temporary images to allow camera to adjust to environment.

    for i in xrange(ramp_frames):
        temp = get_image()

    camera_capture = cv2.cvtColor(get_image(), cv2.COLOR_BGR2GRAY)

    cv2.imwrite("baseCase.jpg", camera_capture)

    time.sleep(3) # delay to allow user to acclimate

    print 'Base case CAPTURED.'

    return camera_capture



def check_presence(prev, current, lowerX, upperX, lowerY, upperY):
    ''' Within a bounded region, check if an object has appeared. '''

    area = abs(lowerX-upperX) * abs(lowerY-upperY)

    diff = cv2.absdiff(prev, current)
    # diffT = zip(*diff)    

    # trueCount is the number of pixels within a region that have changed from the base case.
    trueCount = len( np.where(diff[lowerY:upperY,lowerX:upperX] > 20)[0] )

    percent = trueCount / float(area)

    if percent > 0.30:
        return True


def check_key_press():

    state = 0

    # Start record on space key
    if cv2.waitKey(1) & 0xFF==ord(' '):
        print 'SPACE KEY'
        # state = 1
        # return state

    # Quit record when space is tapped again
    if cv2.waitKey(1) & 0xFF==ord('b'):
        print 'B KEY'
        # state = 0
        # return state

    # Quit window on 'q' key
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cap.release()
        cv2.destroyAllWindows()



def record_audio():
	snare_sound = AudioSegment.from_wav('audio/snare.wav')
	tom_sound = AudioSegment.from_wav('audio/tom.wav')
	combined = snare_sound + tom_sound
	# combined.export("CHECK.wav", format="wav")


def stream_video(base, cap):
    ''' Print matrix of each video frame. '''

    instruments = [
        'snare',
        'hat',
        'tom',
        'bass'
    ]

    # Initialize sounds
    pygame.mixer.init()
    sounds = [pygame.mixer.Sound('audio/' + instr + '.ogg') for instr in instruments]

    playing = [False] * len(sounds)

    positions = [ # xbounds, ybounds
        (37,180, 50,120), # snare
        (37,180, 350,420), # hat
        (467,610, 50,120), # tom
        (467,610, 350,420) # bass
    ]

    colors = [
        (128,114,250),
        (204,50,153),
        (250,128,114),
        (127,255,0)
    ]

    while(cap.isOpened()):      
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1) # mirrored display
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.putText(frame, 'SNARE', (positions[0][0],positions[0][3]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, 5)
        cv2.putText(frame, 'HI HAT', (positions[1][0],positions[1][3]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, 5)
        cv2.putText(frame, 'TOM-TOM', (positions[2][0],positions[2][3]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, 5)
        cv2.putText(frame, 'BASS', (positions[3][0],positions[3][3]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, 5)

        # Check presence of instruments, play audio
        for i, sound in enumerate(sounds):
            if check_presence(base, gray, *positions[i]):
                if not playing[i]:
                    playing[i] = True
                    cv2.rectangle(frame, (positions[i][0], positions[i][2]), (positions[i][1], positions[i][3]), colors[i], -1)
                    sounds[i].play()
            else:
                playing[i] = False

        # play_audio()

        cv2.imshow('frame', frame)

        check_key_press()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()

    # cap = cv2.VideoCapture(0)

    # base_case = get_base_case(cap)
    # stream_video( base_case, cap)

    record_audio()
    # combined.play()