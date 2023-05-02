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

#predict frames from framesQueue
#then puts in resultQueue
def predictGesture(framesQueue, resultsQueue):    
    while 1:
        if framesQueue.empty():
            #TODO framesQueue.gets()
            #TODO resultsQueue.puts()
            print("empty")
        else:
            print("not")
def predictIris(framesQueue, resultsQueue):
    while 1:
        if framesQueue.empty():
            #TODO framesQueue.gets()
            #TODO resultsQueue.puts()
            print("empty")
        else:
            print("not")
        

camera = cv2.VideoCapture(-1)
count = 0
frames_30 = []
numberOfFrames = 30 #TODO should get numberOfFrames from gestures module

resultsQueue_gestures = Queue()
framesQueue_gestures = Queue()

resultsQueue_iris = Queue()
framesQueue_iris = Queue()

gesturesThread = Process(target=predictGesture, args=(framesQueue_gestures, resultsQueue_gestures,))
gesturesThread.start()

gesturesThread = Process(target=predictIris, args=(framesQueue_iris, resultsQueue_iris,))
gesturesThread.start()

while(1):
    success ,frame = camera.read()    
    
    if success:
        frames_30.append(frame)
        count += 1
    
    if count == numberOfFrames:
        framesQueue_iris.put(frames_30)
        framesQueue_gestures.put(frames_30)

        count = 0
        frames_30.clear()
