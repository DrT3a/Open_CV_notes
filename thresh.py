import cv2 as cv

# Load the input image
img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\sorceress.jpg')
cv.imshow('Sorceress', img)
cv.waitKey(0)

# Thresholding is a binarization of an image. You convert it to binary - pixels are either black(0) or white(255)
# We use a thresholding value -> If the pixel intensity is less than the thresholding value we set the pixel to 0, if the pixel intensity is greater than the thresholding value we set the pixel to 255.
# There are two types of thresholding, SIMPLE and ADAPTIVE.

# First we convert this bgr img to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)
cv.waitKey(0)


# __________________Simple Thresholding__________________#
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # Checks each pixel, compares it to 150 and if it is higher it sets it to 255. Then returns two things: Thresh = The thresholded img or binarized and Threshold = the same value we passed (150)
cv.imshow('Simple Thresholded', thresh)
cv.waitKey(0)

# We can create an inverse thesholded img.
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)
cv.waitKey(0)





