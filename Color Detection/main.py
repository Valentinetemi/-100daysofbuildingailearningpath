import cv2 as cv

from color import get_limits

yellow = [0, 255, 255]  #yellow in rgb colorspace

cap = cv.VideoCapture(0)



while True:
    
    ret, frame = cap.read()
    
    hsvImage = cv.cvtColor( frame , cv.COLOR_BGR2HSV )
    
    lower_limit, upper_limit = get_limits(color= yellow)
    
    
    mask = cv.inRange(hsvImage, lower_limit, upper_limit) 
    
    cv.imshow("frame", frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()

cv.destroyAllWindows()
    