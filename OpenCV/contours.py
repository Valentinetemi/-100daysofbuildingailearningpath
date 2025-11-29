import cv2 as cv


img = cv.imread("image6.png")

resized_img = cv.resize(img,(480,360))

ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
resized_img_c = cv.resize(thresh,(480,360))

cv.imshow('img', resized_img)

cv.imshow('thresh', resized_img_c)

cv.waitKey(0)