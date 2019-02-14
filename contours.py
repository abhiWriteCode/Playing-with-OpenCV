import numpy as np
import matplotlib as mplt
import cv2

frame = cv2.imread("images/contour.jpg")
img_w = 400
img_h = frame.shape[0]*img_w//frame.shape[1]
frame = cv2.resize(frame, (img_w, img_h))

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[4]
cv2.imshow('img', img)
op = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

cv2.imshow('op', op)

cv2.waitKey(0)
cv2.destroyAllWindows()