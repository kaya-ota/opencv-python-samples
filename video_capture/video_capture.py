
import cv2
#import skvideo.io

#to quit the program, push ESC key
ESC = 27

#video = "3D_B.JPG"

#video = "SampleVideo_720x480_1mb.mp4"
cap = cv2.VideoCapture(0)
while(True):
	ret, frame = cap.read()
	print(ret)
	if(cap.isOpened()== False):
		print("Error openingvideo stream or file")
	else:
		print("opened successfully")
	cv2.imshow("title", frame)
	if cv2.waitKey(1)==ESC:
		break

    
