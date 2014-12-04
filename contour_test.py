import numpy as np
import cv2 as cv

# cap = cv.VideoCapture(0)

im = cv.imread('images/liani2.jpg') # source image
height, width = im.shape[:2]

blank = np.zeros((height, width, 3),np.uint8)

imgray = cv.cvtColor(im,cv.COLOR_BGR2GRAY) # add gray filter
ret,thresh = cv.threshold(imgray,127,255,0) # idk what this is...-
contours, hierarchy = cv.findContours(thresh, 1, 2)
# contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) # countour approximation

cnt = contours[0]
m = cv.moments(cnt)
# print m

# CALCULATING CENTROID
# cx = int(m['m10']/m['m00'])
# cy = int(m['m01']/m['m00'])

# print cx
# print cy

# print int(m['m10'])
# print int(m['m00'])
# print int(m['m01'])

# DRAW THE CONTOURS
cv.drawContours(blank, contours, -1, (255,255,255), 3)

# SHOW PROCESSED IMAGE
cv.imshow('blank', blank)
k = cv.waitKey()