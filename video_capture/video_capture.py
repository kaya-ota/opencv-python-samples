import cv2
import skvideo.io



video = "test1.mp4"
cap = skvideo.io.VideoCapture(video)
ret, frame = cap.read()

if(cap.isOpened()== False):
    print("Error openingvideo stream or file")
else:
    print("opened successfully")