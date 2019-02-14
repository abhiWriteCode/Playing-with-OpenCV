import numpy as np
import matplotlib as mplt
import cv2

g_img = cv2.imread('images/dirty_img.PNG', cv2.IMREAD_GRAYSCALE)
rtrn, t_img = cv2.threshold(g_img, 10, 255, cv2.THRESH_BINARY)
amt_img = cv2.adaptiveThreshold(g_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)
agt_img = cv2.adaptiveThreshold(g_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 5)

# cv2.imshow('g_img', g_img)
# cv2.imshow('t_img', t_img)
# cv2.imshow('t_img inv', cv2.bitwise_not(t_img))
cv2.imshow('amt_img', amt_img)
cv2.imshow('agt_img', agt_img)

cv2.waitKey(0)
cv2.destroyAllWindows()




# Fuction Details
#
# cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) → dst
#
# Parameters:
# src – Source 8-bit single-channel image.
# dst – Destination image of the same size and the same type as src .
# maxValue – Non-zero value assigned to the pixels for which the condition is satisfied. See the details below.
# adaptiveMethod – Adaptive thresholding algorithm to use, ADAPTIVE_THRESH_MEAN_C or ADAPTIVE_THRESH_GAUSSIAN_C . See the details below.
# thresholdType – Thresholding type that must be either THRESH_BINARY or THRESH_BINARY_INV .
# blockSize – Size of a pixel neighborhood that is used to calculate a threshold value for the pixel: 3, 5, 7, and so on.
# C – Constant subtracted from the mean or weighted mean. Normally, it is positive but may be zero or negative as well.