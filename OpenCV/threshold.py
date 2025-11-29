import cv2



img = cv2.imread("image.png")

resized_img = cv2.resize(img, (800, 700))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized_gray_img = cv2.resize(img_gray, (600, 540))

#ret, thresh =cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,  21,  30)

#ret, thresh =cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)


resized_thresh = cv2.resize(thresh, (600, 540))

cv2.imshow("img", resized_img)
#cv2.imshow("img_gray", resized_gray_img)
cv2.imshow("thresh", resized_thresh)
cv2.waitKey(0)
