import cv2 as cv
import mediapipe as mp
import numpy as np


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

cap = cv.VideoCapture(0)

#Create a canvas to draw the hand landmarks
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

prev_x, prev_y = 0, 0 #stores previous finger positions

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv.flip(frame, 1) #flip the frame horizontally
    
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    #check if hand is detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            #Get index finger landmark (landmark 8)
            
    