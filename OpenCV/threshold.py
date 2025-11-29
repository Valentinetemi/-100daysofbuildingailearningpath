import cv2



img = cv2.imread("spider.jpeg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh =cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("img", img)
cv2.imshow("img_gray", img_gray)
cv2.waitKey(0)
