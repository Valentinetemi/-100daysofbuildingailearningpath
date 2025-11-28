import os

import cv2

img = cv2.imread("lena.jpg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

cv2.imshow("image", img)
cv2.imshow("image rgb", img_rgb)
cv2.imshow("image gray", img_gray)
cv2.imshow("image hsv", img_hsv)
cv2.imshow("image lab", img_lab)
cv2.imshow("image yuv", img_yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()

