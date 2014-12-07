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
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # rectangles(which screen, (top-left corner), (bottom-right corner), (color), size)
    cv.rectangle(gray, (37,80), (180,150), (128,114,250), -1) # Snare
    cv.rectangle(gray, (37,380), (180,450), (204,50,153), -1) # TomTom
    cv.rectangle(gray, (467,80), (593,150), (250,128,114), -1) # Hi Hat
    cv.rectangle(gray, (467,380), (593,450), (127,255,0), -1) # Bass


    font = cv.FONT_HERSHEY_SIMPLEX
    # text(which screen, (position), font type, font scale, (color), thickness, lineType)
    cv.putText(gray, 'SNARE', (50,130), font, 1, BLACK, 2, 5)
    cv.putText(gray, 'HI HAT', (480,130), font, 1, BLACK, 2, 5)
    cv.putText(gray, 'TOM-TOM', (30,430), font, 1, BLACK, 2, 5)
    cv.putText(gray, 'BASS', (490,430), font, 1, BLACK, 2, 5)


    # Display the resulting frame
    cv.imshow('Example', gray)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()