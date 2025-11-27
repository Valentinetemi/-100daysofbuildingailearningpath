import cv2

cap = cv2.VideoCapture(0) # It tells opencv to open the default camera. we are going to use the default camera with is at device index 0, if you have a second camera you use 1, if you have a third camera you use 2 and so on.

while True:
    ret, frame = cap.read() #ret return true if it was able to read the frame correctly, while frame returns an image object. from the camera
    
    cv2.imshow('frame',  frame) # this displays the frame in a window called 'frame', it updates very fast so it looks like a video
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break # this breaks out of the loop when q is pressed


cap.release() #this disposes of the camera resources properly
cv2.destroyAllWindows()