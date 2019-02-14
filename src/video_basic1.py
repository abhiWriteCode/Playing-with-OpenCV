import numpy as np
import matplotlib as mplt
import cv2

capture = cv2.VideoCapture(0) # o for 1st webcam; 1 for external webcam. use can use file name for playing video
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# recording = cv2.VideoWriter('videos/Output.avi', fourcc, 20.0, (640, 480))

while capture.isOpened():
	rtrn, frame = capture.read() # read() return bool and frame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	if rtrn==True:
		# frame = cv2.flip(frame,1)
		# recording.write(frame) # for save video to disk

		cv2.imshow('Frame', frame)
		cv2.imshow('Gray', gray)

		if cv2.waitKey(1) & 0xFF == ord(' '):
			break
	else:
		break

capture.release()
# recording.release()
cv2.destroyAllWindows()