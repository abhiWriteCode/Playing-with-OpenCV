import numpy as np
import matplotlib as mplt
import cv2

img = cv2.imread('images/White_tigers.png', cv2.IMREAD_COLOR)

# Draw Line
cv2.line(img, (0,0), (200, 200), (0,255,0), 15)

# Draw Rectangle
cv2.rectangle(img, (200, 200), (400,300), (255,0,0), 7)

# Draw circle
cv2.circle(img, (400, 500), 100, (0,0,255), -1)

# Draw Polygon
pts = np.array([[155,50], [200,70], [300,10], [450,500]], np.int32)
cv2.polylines(img, [pts], True, (0,0,0), 3)

# Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV rocks!', (550,130), font, 1.9, (255,0,255), 6, cv2.LINE_AA)

cv2.imshow('Edited', img)
cv2.waitKey(0)
cv2.destroyAllWindows()