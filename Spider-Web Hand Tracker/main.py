import cv2 as cv
import mediapipe as mp
import numpy as np


#Initialize mediapipe hands
mp_hands = mp.solutions.hands #this import the hand tracking model
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) #hand create the hand detector/ tracker instance
mp_draw = mp.solutions.drawing_utils #this is lets you draw hand landmark on the video frame.

#start the webcamera

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret :
        break
    
    frame = cv.flip(frame, 1)
    
    #convert bgr to rgb
    rbg_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
    #process the frame to find the hands
    result = hands.process(rbg_frame)
    
    #if the hands are detected
    



