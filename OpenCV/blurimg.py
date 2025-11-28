import os

import cv2

img = cv2.imread("spider.jpeg")

k_size = 7 # the larger the value of kernel size, more blurry it will be and vice versa

cv2.blur(img, (k_size, k_size)) # function to apply blur effect on image

blurred_img = cv2.imwrite("blurred.jpg", img)


cv2.imshow("image", img)
cv2.imshow("Blurred Image", blurred_img)

cv2.waitKey(0)
cv2.destroyAllWindows()