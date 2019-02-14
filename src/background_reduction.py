import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fg = cv2.createBackgroundSubtractorMOG2()

while True:
	_, frame = cap.read()
	fgmask = fg.apply(frame)

	cv2.imshow('original', frame)
	cv2.imshow('fg', fgmask)

	if cv2.waitKey(1) & 0xff == ord(' '):
		break

cap.release()
cv2.destroyAllWindows()