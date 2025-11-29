import cv2 as cv

img = cv.imread("image5.png")

#line
cv.line(img, (100, 150), (300, 450), (0, 255, 0), 3) #line(image, start point, end point, color in BGR format, thickness)



#rectangle 


#circle


#text


cv.imshow("img", img)
cv.waitKey(0)