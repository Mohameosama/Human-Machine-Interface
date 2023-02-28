import mediapipe as mp
import cv2
from tkinter import *
import os
import numpy as np
import csv
import tensorflow as tf
import pandas as pd
#468 to 477 are iris
#size = 32, 42 after iris

rightEyePoints = [33, 7, 246, 163, 161, 160, 144, 159, 145, 158, 153, 157, 154, 173,155, 133]
leftEyePoints = [362, 398, 382, 384, 381, 385, 380, 386, 374, 387, 373, 388, 390, 466, 249, 263]

rightIrisPoints = [468, 469, 470, 471, 472]
leftIrisPoints = [473, 474, 475, 476, 477]

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
mp_drawing_styles = mp.solutions.drawing_styles

draw_specs = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

def get_landmark(image):
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode = True, max_num_faces=1,
                                      refine_landmarks=True, min_detection_confidence=0.5)
    
    image.flags.writeable = False
    result = face_mesh.process(image)
    landmarks = result.multi_face_landmarks[0].landmark
    return result, landmarks

def draw_landmarks(image, result, label):
    image.flags.writeable = True
    if result.multi_face_landmarks:
        for face_landmark in result.multi_face_landmarks:
            height, width, _ = image.shape
            try:
                index = len(os.listdir(f"dataset/{label}"))
            except:
                index = 0
            with open(f'dataset/{label}/{index}.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for i in rightIrisPoints:
                        pt = face_landmark.landmark[i]
                        print(face_landmark.landmark[i].x)
                        tempX = int(pt.x * width)
                        tempY = int(pt.y * height)
                        writer.writerow([face_landmark.landmark[i].x, face_landmark.landmark[i].y, face_landmark.landmark[i].z])
                        
                        # if(i not in numberOfPointsNeeded):
                        cv2.circle(image, (tempX, tempY), 3, (100, 100, 0))
                        # cv2.imshow(f"image {i}", image)
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()
                    
                    # for face_landmark in mp_face_mesh.FACEMESH_IRISES:
                    #     print(face_landmark)
                    #     # pt = face_landmark.landmark
                    #     x = int(face_landmark[0])
                    #     y = int(face_landmark[1])
                        
                    #     cv2.circle(image, (x, y), 3, (100, 100, 0))
                    
    return image

def getData():
    data = []
    directory = f"test.csv"   
    f = os.path.join(directory)                  
    data = pd.read_csv(f'{f}', header=None)

    data = np.array(data)
    # data.resize(1, -1)
    # print(data.size)
    
    return data


def realtimeTest(image, result):
    image.flags.writeable = True
    if result.multi_face_landmarks:
        for face_landmark in result.multi_face_landmarks:
            height, width, _ = image.shape
            with open(f'test.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                # for i in numberOfPointsNeeded:
                #         pt = face_landmark.landmark[i]
                #         print(face_landmark.landmark[i].x)
                #         tempX = int(pt.x * width)
                #         tempY = int(pt.y * height)
                #         writer.writerow([face_landmark.landmark[i].x, face_landmark.landmark[i].y, face_landmark.landmark[i].z])                                                            
    return image


def click1():
        
        
        cam = cv2.VideoCapture(0)
        # reading the input using the camera
        result, image = cam.read()
        result, landmarks = get_landmark(image)
        img = draw_landmarks(image, result, 0)
        cv2.imshow("test", img)
        cv2.waitKey(0)
        cv2.destroyWindow("test")

        # model = tf.keras.models.load_model(f'iris.h5')
        # realtimeTest(image, result)
        # data = getData()
        # res = model.predict(np.expand_dims(data, axis=0))[0]
        # print(f"you looked at {np.argmax(res)}")
        

        
        
def click2():
        cam = cv2.VideoCapture(0)
        # reading the input using the camera
        result, image = cam.read()
        result, landmarks = get_landmark(image)
        img = draw_landmarks(image, result, 1)

        
        
        cv2.imshow("test", img)
        cv2.waitKey(0)
        cv2.destroyWindow("test")
def click3():
        cam = cv2.VideoCapture(0)
        # reading the input using the camera
        result, image = cam.read()
        result, landmarks = get_landmark(image)
        img = draw_landmarks(image, result, 2)

        
        
        cv2.imshow("test", img)
        cv2.waitKey(0)
        cv2.destroyWindow("test")
def click4():
        cam = cv2.VideoCapture(0)
        # reading the input using the camera
        result, image = cam.read()
        result, landmarks = get_landmark(image)
        img = draw_landmarks(image, result, 3)

        
        
        cv2.imshow("test", img)
        cv2.waitKey(0)
        cv2.destroyWindow("test")


# creating main tkinter window/toplevel
master = Tk()

master.attributes('-fullscreen', True)
master.title("Geeks For Geeks")


master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=1)

master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=1)

rectangle_1 = Button(master, text="button 0", bg='yellow', command=click1)
rectangle_1.grid(column=0,row=0, sticky='WENS')

rectangle_2 = Button(master, text="Button 1", bg='blue', command=click2)
rectangle_2.grid(column=0, row=1, sticky="NSEW")

rectangle_3 = Button(master, text="Button 2", bg='red', command=click3)
rectangle_3.grid(column=1, row=0, sticky="NSEW")

rectangle_4 = Button(master, text="Button 3", bg='green', command=click4)
rectangle_4.grid(column=1, row=1, sticky="NSEW")


# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()