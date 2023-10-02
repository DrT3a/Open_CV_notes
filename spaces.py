import cv2 as cv
#import matplotlib.pyplot as plt
# How to switch colorspaces /rgb/grayscale/etc.
img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\scythe.jpg')
cv.imshow('Scythe(BGR)', img)

# plt.imshow(img)
#plt.show()

# Convert from BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Convert from BGR to HSV (hue saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to LAB colorspace (L*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# You can convert all of the above formats/colorspaces and vice versa.
'''You cannot convert Grayscale  to HSV directly. You have to do Grayscale-->BGR--->HSV'''
# HSV to BGR
hsv_bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('hsv_ bgr', hsv_bgr)
#LAB to BGR
lab_bgr = cv.cvtColor(img, cv.COLOR_LAB2BGR)
cv.imshow('lab_bgr', lab_bgr)


cv.waitKey(0)