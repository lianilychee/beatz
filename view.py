### Beatz VIEW

import numpy as np
import cv2

BLACK = (0, 0, 0)

cap = cv2.VideoCapture(0)
img = cv2.imread('snare.png')


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # line(which screen, (start coordinates), (end coordinates), (color), thickness)
    cv2.line(frame, (208,0), (208,480), BLACK, 5)
    cv2.line(frame, (431,0), (431,480), BLACK, 5)    
    # circle(which screen, (center coordinates), (radius), (color), )
    cv2.circle(frame, (50,50), 63, (0,0,255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # text(which screen, (position), font type, font scale, (color), thickness, lineType)
    cv2.putText(frame,'SNARE',(50,50), font, 2, BLACK, 2, 10)

    # Display the resulting frame
    cv2.imshow('Example', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()