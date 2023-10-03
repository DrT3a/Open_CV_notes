import cv2 as cv
import numpy as np

img = cv.imread("E:\Drs\Programming\Open_CV_tutorial\Images\d2_sorceress.jpg")
cv.imshow('Original', img)
cv.waitKey(0)

# Create a blank image with numpy, to reconstuct and show the colors
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)
cv.waitKey(0)

# OpenCV can split an RGB image to its components Red - Green - Blue
# These show the intensity of each color in grayscale. Bright areas have more of each color.
b,g,r = cv.split(img)

# Display only respective B/G/R channels
blue = cv.merge([b,blank,blank]) 
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.waitKey(0)
cv.imshow('Green', green)
cv.waitKey(0)
cv.imshow('Red', red)
cv.waitKey(0)

# Show shapes/dimensions of images and number of colorchannels
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge the channels
merged = cv.merge([b,g,r])
cv.imshow('Merged_Image', merged)

cv.waitKey()