import cv2 as cv

img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\Conan.jpg')
cv.imshow('conan', img)

#Converting to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)



# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)



# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dilated', dilated)

# Eroding (almost revert dilate)
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Croping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)