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

camera = cv2.VideoCapture(0)

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
        