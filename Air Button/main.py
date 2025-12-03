import cv2 as cv
import mediapipe as mp
import numpy as np


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

cap = cv.VideoCapture(0)

#Create a canvas to draw the hand landmarks
canvas = np.zeros((480, 640, 3), dtype=np.uint8) # this is just the black image where we draw the line , later we overlay it on the webcame feed

prev_x, prev_y = 0, 0 #stores previous finger positions

while True:
    ret, frame = cap.read()
    if not ret:
        break # if the frame is not read, break the loop
    
    frame = cv.flip(frame, 1) #flip the frame horizontally
    
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    #check if hand is detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            #Get index finger landmark (landmark 8)
            x = int(hand_landmarks.landmark[8].x * frame.shape[1]) #landmark 8 means = index fingertips, mediapipe gives coordinates in percentage, so we multiply to convert to pixels
            y = int(hand_landmarks.landmark[8].y * frame.shape[0])
            
            #Draw a small dot on the fingertips
            cv.circle(frame, (x, y), 5, (0, 255, 0), -1)
            
            #draw line only if finger moved( not stationary)
            if prev_x != 0  and prev_y != 0:
                cv.line(canvas, (prev_x, prev_y), (x, y), (0, 255, 0), 2) #draw a line from the previous point to the current points
                
            #update previous position
            prev_x, prev_y = x, y
            
    else:
        #If hand disappeared, reset previous points so drawing doesn't jump
        prev_x, prev_y = 0, 0
        
        #combine canvas with original frame
    combined = cv.add(frame, canvas)
        
    cv.imshow('Hand Drawing', combined)
        
    if cv.waitKey(5) & 0xFF == ord('q'):
            break
        
        
cap.release()
cv.destroyAllWindows()
            
    