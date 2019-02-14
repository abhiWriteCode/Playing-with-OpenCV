import numpy as np
import matplotlib as mplt
import cv2

img1 = cv2.imread('images/White_tigers.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('images/Black_horse.png', cv2.IMREAD_COLOR)

rows, columns, channels = img2.shape
roi  = img1[250:rows+250, 460:columns+460] # Region of Image

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

rtrn, mask = cv2.threshold(img2gray, 150, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

dst = cv2.add(img1_bg, img2_fg)
img1[250:rows+250, 460:columns+460] = dst

# Let's visualized
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img2gray', img2gray)
cv2.imshow('mask', mask)  
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()