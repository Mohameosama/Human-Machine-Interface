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

from threading import Thread
import numpy as np
import cv2
import time as t

class ThreadWithReturnValue(Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                            **self._kwargs)
            
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def predictGesture(frames):
    #pre-preprocessing frames
    #predict
    #call the actuator
    # return
    print("it will wait")
    t.sleep(5)
    return 5

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
        gestureThread = ThreadWithReturnValue(target=predictGesture, args=(frames_30, ))    #TODO neglect if no hand in the frame
        # irisThread = ThreadWithReturnValue(target=predictIris, args=(frames_30, ))          #TODO neglect if no face in the frame

        gestureThread.start()
        # irisThread.start()
        
        
        count = 0
        frames_30.clear()
        print (gestureThread.join())
        
