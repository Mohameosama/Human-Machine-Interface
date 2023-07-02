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
# from Gestures.globalModule.globalModule import *
# import Gestures.globalModule.realTest as ges
import gestures as Gesture
import pyautogui
# from cornea.classes.gazeTracker import GazeTracker
from cornea.classes.gazeTracker import GazeTracker

#predict frames from framesQueue
#then puts in resultQueue
def predictGesture(framesQueue, resultsQueue):    
    # frames = []
    gesture = Gesture.gestures()
    while 1:
        if not framesQueue.empty():
            # frames.append(framesQueue.get())
            # if len(frames) >= 30:
                # print("30 frames")
            print(framesQueue.qsize())
            gesture.predict(framesQueue.get())
            # framesQueue = Queue()
                # frames = []
        
        
        # else:
        #     print("no data")


def predictIris(framesQueue, resultsQueue):
    
    gazeTracker = GazeTracker('Models/convModelTest3.h5')

    while 1:

        if not framesQueue.empty():
            frames = framesQueue.get()
            coordinates = gazeTracker.track_gaze(frames)
            pyautogui.moveTo(coordinates[0], coordinates[1])
        else:
            print("no data")
        

camera = cv2.VideoCapture(0)
count = 0
frames_30 = []
numberOfFrames = 30 #TODO should get numberOfFrames from gestures module

resultsQueue_gestures = Queue()
framesQueue_gestures = Queue()

resultsQueue_iris = Queue()
framesQueue_iris = Queue()

gesturesThread = Process(target=predictGesture, args=(framesQueue_gestures, resultsQueue_gestures,))
gesturesThread.start()

# irisThread = Process(target=predictIris, args=(framesQueue_iris, resultsQueue_iris,))
# irisThread.start()

frames_list = []
cv2.waitKey(3000)
while(1):
    success ,frame = camera.read()    
    frames_list.append(frame)    

    if len(frames_list) >= 30 and framesQueue_gestures.qsize() <= 0:
        frames_list = frames_list[-30:]
        # framesQueue_iris.put(frames_list)
        framesQueue_gestures.put(frames_list)
    if len(frames_list) >= 3 and framesQueue_iris.qsize() <= 0:
        temp_frames = frames_list[-3:]
        framesQueue_iris.put(temp_frames)

    # if success:
    #     frames_30.append(frame)
    #     count += 1
    
    # if count == numberOfFrames:
    #     framesQueue_iris.put(frames_30)
    #     framesQueue_gestures.put(frames_30)

    #     count = 0
    #     frames_30.clear()