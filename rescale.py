import cv2 as cv

img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\Conan.jpg')
cv.imshow('Conan', img)
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
def changeres(width,height):
    capture.set(3,width)
    capture.set(4,height)

#Reading Videos

capture = cv.VideoCapture('E:\Drs\Programming\Open_CV_tutorial\Videos\kra.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()