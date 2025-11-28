#What are images : Images are numpy arrays. OpenCV stores images in BGR format.
import cv2

img = cv2.imread('lena.jpg')
print(type(img))

images = cv2.imread('lena.jpg') #how to get image shape
print(images.shape)

#pixel this is where the pixel value of the image, it is where the information about the color of a particular point on an image is stored.
#values of the pixels range from 0 - 255