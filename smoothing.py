import cv2 as cv

img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\helloween.jpg')
cv.imshow('helloween', img)

# Averaging (a method of blurring). The Kernel window computes the center pixel as the average of the surrounding pixels.
average = cv.blur(img, (3,3)) # (nxn) is the kernel size/The higher the kernel the higher the Blur.
cv.imshow('Average_Blur', average)

# Gaussian Blur: Works similarly as averaging except that instead of computing the average of the surrounding pixels, gives a particular weight and then averages Σxi*ni. It looks more naturall.
gauss = cv.GaussianBlur(img, (3,3),0) # SigmaX is the standard deviation in the X direction
cv.imshow('Gaussian_Blur', gauss)

# Median Blur: Same as averaging, but instead of finding the average of surrounding pixels, it finds the median.(Διάμεσος). More effective at reducing noise.
median = cv.medianBlur(img,3) # 7 is the kernel size (you don't need a tuple here)
cv.imshow('Median_Blur', median)

# Bilateral Blur: The most effective and is used in most advanced computer vision projects.Applies blur to the image, while retaining the edges.
bilateral = cv.bilateralFilter(img, 10, 35, 25) # (img, diameter, sigmacolor=larger value means there are more colors in the neighborhood when colors are computed, sigmaspace=larger values means that pixels further out from the center pixel will influence the blurring calculation.)
cv.imshow('Bilateral', bilateral)



cv.waitKey(0)