import cv2 as cv
import numpy as np

img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\woman_face.jpg')
cv.imshow('Original', img)
cv.waitKey(0)

# Masking allows us to focus on certain parts of a image that we'd like to focus on.

blank = np.zeros(img.shape[:2], dtype='uint8') # [:2] ---> The dimentions of the mask must be the same as that of the image. Otherwise it will not work.
cv.imshow('Blank Image', blank)
cv.waitKey(0)

# We will draw a circle over that blank image and call that a mask.
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)
cv.waitKey(0)

# Now lets mask over the image we want. Create masked image
masked = cv.bitwise_and(img, img, mask=mask) # We put one img over the other and found the intersection with the bitwise_AND
cv.imshow('Masked Image', masked)
cv.waitKey(0)