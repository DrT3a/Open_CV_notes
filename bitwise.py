import cv2 as cv
import numpy as np

# MAT is MATRIX

# 4 basic bitwise operators: AND, OR, XOR, NOT. A pixel is turned OFF if it has a value of 0, or turned ON if it has a value of 1.

# Create a blank variable {array of zeros}:
blank = np.zeros((400,400), dtype='uint8')

# Use the blank variable as a basis to draw a rectangle and a circle.
rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)# (copy of the blank varable we created, (starting point), (ending point, color(rbg), thickness;-1 fills the rectangle)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1) #-1 fills the circle

# Display images
#cv.imshow('blank', blank)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND.(Η ΤΟΜΗ στα διαγράμματα Venn) (intersecting regions)
bitwise_and = cv.bitwise_and(rectangle,circle) # We pass the two source images. Overlaps the images and returns the intercept 
cv.imshow('AND', bitwise_and)

# Bitwise OR (H ΕΝΩΣΗ στα διαγράμματα Venn) (non instercecting regions AND intersecting regions)
bitwise_or = cv.bitwise_or(rectangle,circle) # This should overlap and return the intercepting and not intercepting regions.
cv.imshow('OR', bitwise_or)

# Bitwise XOR (Τα μη κοινά στοιχεία {[AUB] - [AՈB]}(Ένωση - Τομή) (non intersecting regions)
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR', bitwise_xor)

# Bitwise NOT (Είναι σαν να λέμε το Συμπλήρωμα) (inverts the binary color)
bitwise_not = cv.bitwise_not(circle)
cv.imshow('NOT', bitwise_not)

cv.waitKey(0)