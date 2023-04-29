"""
The main file for controlling the entire project

Pseudo code
------------

Setup LOOP:
- calibrate
- if calibrated move on to normal loop

Normal LOOP:
- load models
- START LOOP
    - capture frames 
    - create thread for iris, returns grid location
    - create thread for gesture, returns gesture
    - wait for both threads to join
    - decision making with both inputs
    - run appropriate decision with actuator

"""

import threading as th
import numpy as np
import cv2

def predictGesture(frames):
    #pre-preprocessing frames
    #predict
    #call the actuator
    return

def predictIris(frames):
    return

camera = cv2.VideoCapture(-1)
count = 0
frames_30 = []
numberOfFrames = 30 #TODO should get numberOfFrames from gestures module




while(1):
    success ,frame = camera.read()    
    
    if success:
        frames_30.append(frame)
        count += 1
    
    if count == numberOfFrames:
        
        #TODO neglect if no face in the frame
        gestureThread = th.Thread(target=predictGesture, args=(frames_30, ))    #TODO neglect if no hand in the frame
        irisThread = th.Thread(target=predictIris, args=(frames_30, ))          #TODO neglect if no face in the frame

        gestureThread.start()
        irisThread.start()
        
        count = 0
        frames_30.clear()
        
        