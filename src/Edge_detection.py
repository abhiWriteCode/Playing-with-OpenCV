import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
	edge = cv2.Canny(frame, 100, 100) # 2nd and 3rd args are our minVal and maxVal respectively


	# threshold the image by setting all pixel values less than 128 to 255 (white; foreground)
	# and all pixel values >= 128 to 255 (black; background), thereby segmenting the image
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	_, threshold = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV) # cv2.THRESH_BINARY

	# cv2.imshow('Original', frame)
	# cv2.imshow('Laplacian', laplacian)
	# cv2.imshow('sobel x', sobelx)
	# cv2.imshow('sobel y', sobely)
	cv2.imshow('edge1', edge)
	cv2.imshow("Gray", gray)
	cv2.imshow("Thresh", threshold)

	if cv2.waitKey(5) & 0xFF == 32: # if press SPACE bar
		break

cap.release()
cv2.destroyAllWindows()