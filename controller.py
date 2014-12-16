import cv2 
import cv
import numpy as np
import time
import pygame

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

    if percent > 0.50:
        return True



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
    positions = [
        (37,180, 80,150),
        (37,180, 380,450),
        (467,610, 80,150),
        (467,610, 380,450)
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

        cv2.putText(frame, 'SNARE', (50,130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, 5)
        cv2.putText(frame, 'TOM-TOM', (480,130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, 5)
        cv2.putText(frame, 'HI HAT', (30,430), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, 5)
        cv2.putText(frame, 'BASS', (490,430), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, 5)

        # Check presence of instruments, play sounds
        for i, sound in enumerate(sounds):
            if check_presence(base, gray, *positions[i]):
                if not playing[i]:
                    playing[i] = True
                    cv2.rectangle(frame, (positions[i][0], positions[i][2]), (positions[i][1], positions[i][3]), colors[i], -1)
                    sounds[i].play()
            else:
                playing[i] = False

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()



if __name__ == '__main__':
    pygame.init()

    cap = cv2.VideoCapture(0)

    base_case = get_base_case(cap)
    stream_video( base_case, cap)