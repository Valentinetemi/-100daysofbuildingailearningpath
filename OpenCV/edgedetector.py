import cv2 as cv

import numpy as np

img = cv.imread("Image3.jpg")

img_edge = cv.Canny(img, 100, 200)

img_edge_d = cv.dilate(img_edge, np.ones((5, 5), dtype=np.int8))

img_edge_e = cv.erode(img_edge, np.ones((5, 5), dtype=np.int8))

cv.imshow("img", img)
cv.imshow("img_edge", img_edge)
cv.imshow("dilate_img", img_edge_d)
cv.imshow("erode", img_edge_e)
cv.waitKey(0)

