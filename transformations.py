import cv2 as cv
import numpy as np

img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\drow.png')
cv.imshow('Original', img)

# Translation: Shifting an Image along the x,y axis or any combination of the above
def translate(img, x, y): # x, y is the number of pixels
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) # img.shape[1] = width, img.shape[0] = height
    return cv.warpAffine(img, transMat, dimensions)

# -x ---> left
# -y ---> Up
# x ---> Right
# y ---> Down
# Essentially Translate shifts YOUR VIEW relative to the img.
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)
cv.waitKey(0)

# Rotation
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat  =  cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)
cv.waitKey(0)

# You can also rotate an already rotated img:
rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated_Rotated', rotated_rotated)
cv.waitKey(0)

# Resizing 
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
cv.waitKey(0)

# Flipping
flip = cv.flip(img, -1) 
# 0 = flip vertically
# 1 = flip horizontally
# -1 = flip vertically and horizontally
cv.imshow('Flip', flip)
cv.waitKey(0)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)