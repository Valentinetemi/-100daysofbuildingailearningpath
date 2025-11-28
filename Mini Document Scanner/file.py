import os

import cv2

img = cv2.imread("image.png") #to check if image exists 
if img is None:
    raise SystemError("Image does not exit")

h, w = img.shape[:2] #print orignal shape
print(f"Original Size, {w}x{h}")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #covert to grayscale


blur = cv2.GaussianBlur(gray, ( 18, 18),0) #to blur the image and reduce noise

_, scanned = cv2.threshold(blur, 0, 1, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # to convert from grayscale to binary image

new_width =500
new_height = 600
scanned_resize = cv2.resize(img, (new_width, new_height))

cv2.imshow("Original size", img)
cv2.imshow("Scanned Image", scanned_resize)
cv2.imwrite("Scanned_output.png", scanned_resize)
print('Saved Scanned Image ')
cv2.waitKey(0)
cv2.destroyAllWindows
