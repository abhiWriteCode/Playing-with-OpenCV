import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# _, threshold = cv2.threshold(gray, 144, 255, cv2.THRESH_BINARY_INV)
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

	cv2.imshow('Original', frame)
	# cv2.imshow('gray', gray)
	# cv2.imshow('threshold', threshold)
	cv2.imshow('Laplacian', laplacian)
	cv2.imshow('sobel x', sobelx)
	cv2.imshow('sobel y', sobely)
	cv2.imshow('sobel X+Y', cv2.add(sobelx,sobely))
	

	if cv2.waitKey(5) & 0xFF == 32: # if press SPACE bar
		break

cap.release()
cv2.destroyAllWindows()