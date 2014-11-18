import numpy as np
import cv2 as cv

im = cv.imread('images/liani.jpg') # source image
height, width = im.shape[:2]

blank = np.zeros((height, width, 3),np.uint8)

imgray = cv.cvtColor(im,cv.COLOR_BGR2GRAY) # add gray filter
ret,thresh = cv.threshold(imgray,127,255,0) # idk what this is...
contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) # countour approximation

# draw the contours
cv.drawContours(im, contours, -1, (0,255,0), 3)

# show the processed image
cv.imshow('imgray', im)
cv.imshow('blank', blank)
k = cv.waitKey()