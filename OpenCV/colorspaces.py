import os

import cv2

img = cv2.imread("lena.jpg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("image", img)
cv2.imshow("image rgb", img_rgb)
cv2.imshow("image gray", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

