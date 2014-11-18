import numpy as np
import cv2 as cv

im = cv.imread('liani.jpg') # source image

# while(1):
imgray = cv.cvtColor(im,cv.COLOR_BGR2GRAY) # add gray filter
ret,thresh = cv.threshold(imgray,127,255,0) # idk what this is...
contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) # countour approximation

# draw the dang contours
cv.drawContours(im, contours, -1, (0,255,0), 3)

cv.imshow('imgray', im)
k = cv.waitKey()
	# if k ==27:
	# 	break

# cv.destroyAllWindows()