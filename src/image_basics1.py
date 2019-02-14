import numpy as np
import matplotlib as mplt # matplotlib use RGB format
import cv2 # opencv use BGR format

img = cv2.imread('images/Black_horse.png', cv2.IMREAD_GRAYSCALE)
# value of IMREAD_GRAYSCALE is 0
# value of IMREAD_COLOR is 1
# value of IMREAD_UNCHANGED is -1

cv2.imshow('Black Horse', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('images/Black_horse_grayscale.png', img) # save image