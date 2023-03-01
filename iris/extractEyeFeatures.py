import mediapipe as mp
import cv2
from tkinter import *
import os
import numpy as np
import csv
import tensorflow as tf
import pandas as pd
import math

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

def euclideanDistance(x1, y1, x2 ,y2):
     return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

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
                
                for eyePoint in rightEyePoints:
                     for irisPoint in rightIrisPoints:
                          writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[irisPoint].x, face_landmark.landmark[irisPoint].y)] )
                for eyePoint in leftEyePoints:
                     for irisPoint in leftIrisPoints:
                          writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[irisPoint].x, face_landmark.landmark[irisPoint].y)] )
            
    return image

def test_realtime(image, result):
    
    model = tf.keras.models.load_model(f'iris.h5')

    image.flags.writeable = True
    if result.multi_face_landmarks:
        for face_landmark in result.multi_face_landmarks:
            height, width, _ = image.shape
            with open(f'test.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for eyePoint in rightEyePoints:
                     for irisPoint in rightIrisPoints:
                          writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[irisPoint].x, face_landmark.landmark[irisPoint].y)] )
                for eyePoint in leftEyePoints:
                     for irisPoint in leftIrisPoints:
                          writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[irisPoint].x, face_landmark.landmark[irisPoint].y)] )                                                           

    data = []
    directory = f"test.csv"   
    f = os.path.join(directory)                  
    data = pd.read_csv(f'{f}', header=None)
    data = np.array(data)
    res = model.predict(np.expand_dims(data, axis=0))[0]
    print(f"you looked at {np.argmax(res)}")
    # return image


def click(label):
    
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    result, landmarks = get_landmark(image)
    
    
    
    ###################THIS FOR TESTING###################
    # test_realtime(image, result)

    ###################THIS FOR COLLECTING DATA###################
    img = draw_landmarks(image, result, label)


master = Tk()

master.attributes('-fullscreen', True)
master.title("IRIS control")


master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=1)

master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=1)

rectangle_1 = Button(master, text="button 0", bg='yellow', command= lambda: click(0))
rectangle_1.grid(column=0,row=0, sticky='NSEW')

rectangle_2 = Button(master, text="Button 1", bg='blue', command= lambda: click(1))
rectangle_2.grid(column=0, row=1, sticky="NSEW")

rectangle_3 = Button(master, text="Button 2", bg='red', command= lambda: click(2))
rectangle_3.grid(column=1, row=0, sticky="NSEW")

rectangle_4 = Button(master, text="Button 3", bg='green', command= lambda: click(3))
rectangle_4.grid(column=1, row=1, sticky="NSEW")


mainloop()