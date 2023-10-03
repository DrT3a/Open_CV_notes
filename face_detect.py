import cv2 as cv

# Import image with a face
# img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\woman_face.jpg')
# cv.imshow('Original', img)
# cv.waitKey(0)

# Import image with five faces
img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\group_of_5.jpg')
cv.imshow('Group', img)
cv.waitKey(0)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)

# Read the haar_face.xml file. Set it in a variable and pass the path.
# The haar_face.xml was obtained from OpenCV github.
haar_cascade = cv.CascadeClassifier('haar_face.xml') # Reads all 33k lines of code in haar_face.xml and stores them in the haar_cascade variable.

# Detect the face in the image.
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=11)
# minNeighbors specifies the number of neighbors a rectangle should have to be called a face.
# The detectMultiScale takes the gray img, uses the variables scaleFactor and minNeighbors, to detect a face and return the rectangular coordinates of that face as a LIST to faces_rect.

# We can print the number of rectangles using len()
print(f'Number of faces found = {len(faces_rect)}')

# Since faces_rect are the rectangular coordinates for the faces that are present in the img we can loop over this list and grab the coordinates of those images and draw a rectangle over the detected faces.
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2) # point1:(x,y), point2:(x+w,y+h)

cv.imshow('Detected Faces', img)
cv.waitKey(0)

# We see that it detects 8 faces instead of 5 (using scaleFactor=1.1, minNeighbors=3). That is because hardcascades are really sensitive to noise. If we want to minimise noise sensitivity is to tweak scaleFactor and min Neighbors.
# Testing the values we find using minNeighbors=11 finds the correct amount of faces.

# Haar cascades is not for advanced projects but is easy to use. It can also be used for video, where the whole thing applies on a frame by frame basis.