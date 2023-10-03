import cv2 as cv
import numpy as np

# Gradients and Edge detection are completely different from a mathematical point of view, but programmatically you can get away thinking of them as similar. We have already used Canny edge detection that is a multistep method. Here we discuss two gradient methods.
img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\d2_sorceress.jpg')
cv.imshow('Original', img)
cv.waitKey(0)

#__________________Laplacian method____________________#

# Convert the original image to grayscale.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)
cv.waitKey(0)

# Define variable for Laplacian transformation, takes in a source img and applies datadepth
lap = cv.Laplacian(gray, cv.CV_64F) # Computes two gradiens of the grayscale img.
# Images cannot have negative pixel values so we compute the absolute value of that img * all of the pixels of that img are converted to their absolute values* and then we convert that to uint8:image specific datatype.
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)
cv.waitKey(0)

#_________________Sobel Gradient Magnitude Representation____________#
# Sobel computes gradients on two directions the X and Y.
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('Sobelx', sobelx)
cv.waitKey(0)
cv.imshow('Sobely', sobely)
cv.waitKey(0)

# We can also get the combined sobel img by combining sobelx adn sobely. We combine using bitwise_or (Ένωση Venn)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)
cv.waitKey(0)

# Lets compare to Canny edge detection.
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)