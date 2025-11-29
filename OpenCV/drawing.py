import cv2 as cv

img = cv.imread("image5.png")
print(img.shape)

#line
cv.line(img, (100, 150), (300, 450), (0, 255, 0), 10) #line(image, start point, end point, color in BGR format, thickness)


#rectangle 
cv.rectangle(img, (100, 150), (300, 450), (0, 0, 255), 5) #-1 for fill the rectangle with given color))


#circle
cv.circle(img, (200, 300), 170, (255, 0, 0), 10) #circle(image, center of circle, radius, color in BGR format, thickness)


#text
cv.putText(img, "Hello World!", (100, 200), cv.FONT_HERSHEY_COMPLEX_SMALL, 2.5, (255, 255, 0), 8) #putText(image, text to be written on image, position where we want to write it, font type and size, color in BGR format, thickness)


cv.imshow("img", img)
cv.waitKey(0)