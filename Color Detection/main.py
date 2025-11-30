import cv2 as cv

cap = cv.VideoCapture(0)



while True:
    
    ret, frame = cap.read()
    
    cv2.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    cv.imshow("frame", frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()

cv.destroyAllWindows()
    