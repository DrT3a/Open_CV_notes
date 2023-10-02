import cv2 as cv

img = cv.imread('E:\Drs\Programming\Open_CV_tutorial\Images\Conan.jpg')

cv.imshow('Conan', img)

# cv.waitKey(0)

#Reading Videos

# capture = cv.VideoCapture('E:\Drs\Programming\Open_CV_tutorial\Videos\kra.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()