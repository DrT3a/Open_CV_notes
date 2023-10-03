import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
cv.waitKey(0)

# 1.Paint the image a certain colour
blank[200:300, 300:400] = 0,0,255
cv.imshow('Green', blank)
cv.waitKey(0)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)
cv.waitKey(0)

# 3. Draw a Circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)
cv.waitKey(0)

# 4.Draw a Line
cv.line(blank, (0,0), (500,500), (255,255,255), thickness=3)
cv.imshow('Line', blank)
cv.waitKey(0)

# 5.Write text on an Image
cv.putText(blank, 'Hello World', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)