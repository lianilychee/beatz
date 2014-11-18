import numpy as np
import cv2 as cv

im = cv.imread('liani.jpg') # source image

for h,cnt in enumerate(contours):
    mask = np.zeros(imgray.shape,np.uint8)
    cv2.drawContours(mask,[cnt],0,255,-1)
    mean = cv2.mean(im,mask = mask)

cv.imshow('imgray', im)
k = cv.waitKey()