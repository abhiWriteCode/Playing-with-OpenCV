import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('xml/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('xml/haarcascade_smile.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
	_, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)
		cv2.putText(frame, 'Face', (x,y), font, 0.9, (255,255,255), 1, cv2.LINE_AA)

		eye_color_face_roi = frame[y+h//3:y+2*h//3, x:x+w]
		eye_gray_face_roi = gray[y+h//3:y+2*h//3, x:x+w]
		eyes = eye_cascade.detectMultiScale(eye_gray_face_roi)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(eye_color_face_roi, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
			cv2.putText(frame, 'Eye', (x+ex,y+h//3+ey), font, 0.7, (255,255,255), 1, cv2.LINE_AA)

		smile_color_face_roi = frame[y+2*h//3:y+h, x:x+w]
		smile_gray_face_roi = gray[y+2*h//3:y+h, x:x+w]
		smiles = smile_cascade.detectMultiScale(smile_gray_face_roi)
		for (sx,sy,sw,sh) in smiles:
			cv2.rectangle(smile_color_face_roi, (sx,sy), (sx+sw,sy+sh), (0,255,255), 2)
			cv2.putText(frame, 'Smile', (x+sx,y+h*2//3+sy), font, 0.7, (255,255,255), 1, cv2.LINE_AA)

		cv2.imshow('Detector',frame)

	if cv2.waitKey(30) & 0xff == ord(' '):
		break
		
cap.release()
cv2.destroyAllWindows()