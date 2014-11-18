import numpy as np
import cv2 as cv

im = cv.imread('liani.jpg') # source image

imgray = cv.cvtColor(im,cv.COLOR_BGR2GRAY) # add gray filter
ret,thresh = cv.threshold(imgray,127,255,0) # idk what this is...
contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) # countour approximation

# draw the contours
cv.drawContours(im, contours, -1, (0,255,0), 3)

# mask the image
for h, cnt in enumerate(contours):
	mask = np.zeros(imgray.shape,np.uint8)
	cv.drawContours(mask,[cnt],0,255,-1)
	mean = cv.mean(im, mask = mask)

# show the processed image
cv.imshow('imgray', im)
k = cv.waitKey()