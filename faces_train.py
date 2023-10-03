import os
import cv2 as cv
import numpy as np

# We will train opencv built in recogniser on all the images, like building a mini-deep-learning model by using opencv face recogniser.

# Create a list of all the people in the folder using their folder names.
# we can either manually enter the names like a caveman.
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# or we can create an empty list and loop through every folder in the apropriate dir.
p = []
for i in os.listdir(r'E:\Drs\Programming\Open_CV_tutorial\Images\Faces\train'):
    p.append(i)

print(p) # Much much Better!

# Create variable named DIR and set it equal to the base folder.
DIR = r'E:\Drs\Programming\Open_CV_tutorial\Images\Faces\train'

# Now we create a function to loop through every folder in the base folder and  subfolder and loop through every img and grab every img and add that to our training set.
# The training set will consist of two lists: features = [] and the corresponding labels = [], so for every face in the feature list, who is the corresponding label (whos face does it belong to.)

# Now we will try to detect the faces in the images. We can copy paste the code from the previous lesson on face detect (haar_cascade classifier)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []
def create_train(): 
    for person in people:
        path = os.path.join(DIR, person) # For every folder in DIR we grab each subfolder.
        label = people.index(person)
        # Now that we are inside each folder we will loop over every image in that folder
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            # Now that we have the path to every img we will read that img from this path 
            img_array = cv.imread(img_path)
            # Convert to Grayscale
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            # Detect the face in the img.Create our faces_rect like previously
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            # Now we loop over every face in this array/faces_rect:
            for (x,y,w,h) in faces_rect:
                # Grab the faces Region of Interest and crop out the face in the image.
                faces_roi = gray[y:y+h, x:x+w]
                # Now that we have a face region of interest we can append that to the features list and the corresponding label to the label list.
                features.append(faces_roi)
                labels.append(label) # The label variable is the essentially the index of the list people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']. The idea of converting the label to numerical values is to reduce the strain that the computer will have by mapping the string and a numerical label.The maping we do is the INDEX of that particular list.i.e. Ben Afflec index:0, Elton John index:1 etc.
# Run this
create_train()
print('--------------Training done-------------')

print(f'Length of the features list = {len(features )}')
print(f'Length of the labels list = {len(labels)}')

# Before training we convert features and labels lists to numpy arrays.
features = np.array(features, dtype='object') # Set datatype object for homogenity
labels = np.array(labels)

# Now that we have appended the images and labels to the corresponding lists we can train our recogniser on it.
# Instantiate our face recogniser
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and labels list.
face_recognizer.train(features, labels)

# Save an array to a binary file in NumPy .npy format.
np.save('features.npy', features)
np.save('labels.npy', labels)

# Now the face recogniser is trained and we can use this. The problem is; if we plan to use this model/recogniser on another file we have to separately and manually repeat this proccess.
# However opencv allows us to save this model so we can use it on another file/directory/part of the world.
face_recognizer.save('face_trained.yml') # path to yaml source file

# Next we use this model to actually recognise images, see: face_recognition.py