import os

import cv2
from numpy import resize

image = cv2.imread('lena.jpg')

print(image.shape)

resize_image = cv2.resize(image, (420, 200))

cv2.imshow("resize_image", resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()