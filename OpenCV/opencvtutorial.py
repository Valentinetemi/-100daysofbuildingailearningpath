# opencv-tutorial
import cv2

img = cv2.imread('lena.jpg', -1)

print(img)

ESC_KEY = 27

img1 = cv2.imshow('image', img)
k = cv2.waitKey(0) #we will capyure the key press and then close it and destroy all windows

if k == ESC_KEY: 
    cv2.destroyAllWindows()
    
elif k == ord('s'):
    img2 = cv2.imwrite('lena_copy.jpg', img ) #we use the same image we save as the one we want to write a cpoy for
    cv2.destroyAllWindows()