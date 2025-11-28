#What are images : Images are numpy arrays. OpenCV stores images in BGR format.
import cv2

img = cv2.imread('lena.jpg')
print(type(img))

images = cv2.imread('lena.jpg')
print(images.shape)