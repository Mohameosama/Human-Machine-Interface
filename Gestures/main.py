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


from multiprocessing import Process, Queue
import cv2
import gestures as Gesture
import pyautogui
from cornea.classes.gazeTracker import GazeTracker
import mediapipe as mp
import numpy as np

def predictGesture(framesQueue, resultsQueue):    
    # frames = []
    gesture = Gesture.gestures()
    while 1:
        if not framesQueue.empty():
            print(framesQueue.qsize())
            gesture.predict(framesQueue.get())

def predictIris(framesQueue, resultsQueue):
    
    gazeTracker = GazeTracker('Models/convModelTest3.h5')

    while 1:
        if not framesQueue.empty():
            frames = framesQueue.get()
            coordinates = gazeTracker.track_gaze(frames)
            pyautogui.moveTo(coordinates[0], coordinates[1])

camera = cv2.VideoCapture(2)











mpHolistics = mp.solutions.holistic
def isHandFound(frame):    
    
    with mpHolistics.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        results = holistic.process(frame)
        if results.right_hand_landmarks == None:
            return False
        else:
            return True
        










numberOfFrames = 30 #TODO should get numberOfFrames from gestures module

framesQueue_gestures = Queue()
resultsQueue_gestures = Queue()

framesQueue_iris = Queue()
resultsQueue_iris = Queue()


gesturesThread = Process(target=predictGesture, args=(framesQueue_gestures, resultsQueue_gestures,))
gesturesThread.start()

irisThread = Process(target=predictIris, args=(framesQueue_iris, resultsQueue_iris,))
irisThread.start()

frames_list = []

cv2.waitKey(3000)  # wait 3 seconds to load the whole project and threads

mpHands = mp.solutions.hands
hands = mpHands.Hands()
handFramesCount = 0


while(1):
    success ,frame = camera.read()   
    cv2.imshow("camera", frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frames_list.append(frame)

    # Check if hand is found on frame or not
    imageRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    if results.multi_hand_landmarks:
        handFramesCount += 1
    else:
        handFramesCount = 0

    if handFramesCount == 30 and framesQueue_gestures.qsize() <= 0:        
        
        frames_list = frames_list[-30:]        
        framesQueue_gestures.put(frames_list)

       

    # if len(frames_list) >= 30 and framesQueue_gestures.qsize() <= 0:
    #     frames_list = frames_list[-30:]
    #     # framesQueue_iris.put(frames_list)
    #     framesQueue_gestures.put(frames_list)


    if len(frames_list) >= 3 and framesQueue_iris.qsize() <= 0:
        temp_frames = frames_list[-3:]
        framesQueue_iris.put(temp_frames)

cv2.destroyAllWindows()
