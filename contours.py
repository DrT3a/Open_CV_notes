import cv2 as cv
import numpy as np

img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\drow.png')
cv.imshow('Original', img)

# Create a blank image
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
cv.waitKey(0)

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)

# Blur the image before
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
cv.waitKey(0)

# # Grab the edges of the image using canny
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
cv.waitKey(0)

#ret,thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)# Takes an img and converts to binary
# cv.imshow('Canny',canny)

# Find the contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Draw the contours over the bland img at line 7
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)