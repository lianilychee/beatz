### Beatz VIEW

import numpy as np
import cv2 as cv

BLACK = (0, 0, 0)

cap = cv.VideoCapture(0)
img = cv.imread('snare.png')


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # line(which screen, (start coordinates), (end coordinates), (color), thickness)
    # cv.line(frame, (208,0), (208,480), BLACK, 5)
    # cv.line(frame, (431,0), (431,480), BLACK, 5)    

    # circle(which screen, (center coordinates), (radius), (color), )
    # cv.circle(frame, (100,200), 63, (128,114,250), -1)
    # cv.circle(frame, (530,200), 63, (250,128,114), -1)    

    # rectangles(which screen, (top-left corner), (bottom-right corner), (color), size)
    cv.rectangle(frame, (37,80), (163,150), (128,114,250), -1) # Snare
    cv.rectangle(frame, (25,380), (180,450), (204,50,153), -1) # TomTom
    cv.rectangle(frame, (467,80), (593,150), (250,128,114), -1) # Hi Hat
    cv.rectangle(frame, (467,380), (593,450), (127,255,0), -1) # Bass


    font = cv.FONT_HERSHEY_SIMPLEX
    # text(which screen, (position), font type, font scale, (color), thickness, lineType)
    cv.putText(frame, 'SNARE', (50,130), font, 1, BLACK, 2, 5)
    cv.putText(frame, 'HI HAT', (480,130), font, 1, BLACK, 2, 5)
    cv.putText(frame, 'TOM-TOM', (30,430), font, 1, BLACK, 2, 5)
    cv.putText(frame, 'BASS', (490,430), font, 1, BLACK, 2, 5)


    # Display the resulting frame
    cv.imshow('Example', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()