import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Hue Staturated Vakue

	lower_red = np.array([0,0,0])
	upper_red = np.array([100,255,255])

	mask = cv2.inRange(hsv, lower_red, upper_red)
	result = cv2.bitwise_and(frame, frame, mask=mask)

	kernel = np.ones((15,15), np.float32) / (15*15)
	smoothed = cv2.filter2D(result, -1, kernel)
	blur = cv2.GaussianBlur(result, (5, 5), 0)
	median = cv2.medianBlur(result, 15)
	bilateral = cv2.bilateralFilter(result, 15, 75, 75)

	cv2.imshow('frame', frame)
	# cv2.imshow('hsv', hsv)
	# cv2.imshow('mask', mask)
	# cv2.imshow('result', result)
	# cv2.imshow('smoothed', smoothed)
	cv2.imshow('blur', blur)
	# cv2.imshow('median', median)
	# cv2.imshow('bilateral', bilateral)

	if cv2.waitKey(5) & 0xFF == 32: # if press SPACE bar
		break

cap.release()
cv2.destroyAllWindows()