import os

import cv2

img = cv2.imread('lena.jpg')

print(img.shape)



cropped_img = img[300:360, 450:500]

cv2.imshow("Image", cropped_img)
print(cropped_img.shape)

cv2.waitKey(0)
        
cv2.destroyAllWindows()
