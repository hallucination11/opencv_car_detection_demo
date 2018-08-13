import cv2 as cv
import numpy as np


def face_detect_demo(image):

	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	face_detector = cv.CascadeClassifier("C:/Users/Chen Songsong/Desktop/python/opencv/haarcascades/haarcascade_frontalface_alt2.xml")

	faces = face_detector.detectMultiScale(gray, 1.01, 5 )
	print(faces)
	for x, y, w, h in faces:
		cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2) #画红色矩形 线宽为2
	cv.imshow("result", image)
	



#src = cv.imread("C:/Users/Chen Songsong/Desktop/python/opencv/lena.jpg")
#print(src)
capture = cv.VideoCapture(0)

#cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)

#cv.imshow("input image", src)

while(True):
	ret, frame = capture.read()
	frame = cv.flip(frame, 1)
	face_detect_demo(frame)
	c = cv.waitKey(10)
	if c == 27:
		break

cv.waitKey(0)

cv.destroyAllWindows()
