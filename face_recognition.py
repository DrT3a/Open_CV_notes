import numpy as np
import cv2 as cv

# Create our haar file
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# # Load features and labels array
# features = np.load('features.npy', allow_pickle= 'True')
# labels = np.load('labels.npy')

# Get the mapping 
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# Read the face_trained.yml file. [YAML is a human-readable data-serialization language. It is commonly used for configuration files and in applications where data is being stored or transmitted.]
# Instantiate our face recogniser
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# Create a variable and give it a path from the validation image set folder.
img = cv.imread(r'E:\Drs\Programming\Open_CV_tutorial\Images\Faces\val\elton_john\1.jpg')

# Covert it to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Unidentified person', gray)
cv.waitKey(0)

# First we detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
# Loop through every face in faces_rect
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h] # Grab the region of interest
    label, confidence = face_recognizer.predict(faces_roi)  # Predict using this face recogniser
    print(f'Label = {people[label]} with a confidence of {confidence}')
    
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2) # Add text on the image
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2) # Draw a rectangle over the face

# Display the image
cv.imshow('Detected Face', img)
cv.waitKey(0)


