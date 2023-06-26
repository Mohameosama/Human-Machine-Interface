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
            framesQueue = Queue()
                # frames = []
        
        
        # else:
        #     print("no data")


def predictIris(framesQueue, resultsQueue):
    while 1:
        if framesQueue.empty():
            #TODO framesQueue.gets()
            #TODO resultsQueue.puts()
            print("empty")
        else:
            print("no data")
        

camera = cv2.VideoCapture(1)
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
    frames_list = frames_list[-30:]

    if len(frames_list) >= 30:
        framesQueue_iris.put(frames_list)
        framesQueue_gestures.put(frames_list)

    # if success:
    #     frames_30.append(frame)
    #     count += 1
    
    # if count == numberOfFrames:
    #     framesQueue_iris.put(frames_30)
    #     framesQueue_gestures.put(frames_30)

    #     count = 0
    #     frames_30.clear()