import cv2 as cv

img = cv.imread("image5.png")
print(img.shape)

#line
cv.line(img, (100, 150), (300, 450), (0, 255, 0), 10) #line(image, start point, end point, color in BGR format, thickness)


#rectangle 
cv.rectangle(img, (100, 150), (300, 450), (0, 0, 255), 5) #-1 for fill the rectangle with given color))


#circle
cv.circle(img, (600, 700), 100, (0, 255, 255), 6) #circle(image, center of circle, radius, color in BGR format, thickness)


#text


cv.imshow("img", img)
cv.waitKey(0)