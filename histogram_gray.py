import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\d2_sorceress.jpg')
cv.imshow('Sorc', img)

# Histograms allow to visualise the distribution of pixel intensity in an image.

# # -------Histograms for grayscale---------#

# # Lets convert the original img to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale', gray)
# # Compute the grayscale histogram 
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# # Plot it with pyplot
# plt.figure()
# plt.title('Grayscale Histogram') # Give it a title
# plt.xlabel('Bins') # Label of x axis = THE INTERVALS OF PIXEL INTENSITIES = THE INTENSITY OF THE PIXELS
# plt.ylabel('# of pixels') # Label of y axis
# plt.plot(gray_hist) # plot it
# plt.xlim([0,256]) # give it a limit along the x axis
# plt.show() # display img


#-------------Create Mask and Compute Histogram for it-----------------#

# Create a blank image
blank = np.zeros(img.shape[:2], dtype='uint8') # Image of shape of first two values so that the images are the same (width, height) I assume....
 
# Lets convert the original img to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# We will draw a circle over that blank image and call that a mask.
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

# Now lets mask over the image we want. Create masked image
masked = cv.bitwise_and(gray, gray, mask=mask) # We put one img over the other and found the intersection with the bitwise_AND
cv.imshow('Masked Image', masked)

# Compute the grayscale histogram 
gray_hist = cv.calcHist([gray], [0], masked, [256], [0,256]) # We set the mask parameter to mask variable that we set before.

# Plot it with pyplot
plt.figure()
plt.title('Grayscale Histogram') # Give it a title
plt.xlabel('Bins') # Label of x axis = THE INTERVALS OF PIXEL INTENSITIES = THE INTENSITY OF THE PIXELS
plt.ylabel('# of pixels') # Label of y axis
plt.plot(gray_hist) # plot it
plt.xlim([0,256]) # give it a limit along the x axis
plt.show() # display img


cv.waitKey(0)
