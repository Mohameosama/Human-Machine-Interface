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

roundedFacePoints = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109]
extraPoints = [468, 473, 127, 10, 356, 152]

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

def euclideanDistance(x1, y1, z1, x2 ,y2, z2):
     z2 = 0
     return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 + (z1 -z2)**2 )

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
                
                for point in rightIrisPoints:
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0, 0.5, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0.5, 0, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 1, 0.5, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0.5, 1, 0)] )
                
                for point in rightIrisPoints:
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0, 0.5, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0.5, 0, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 1, 0.5, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0.5, 1, 0)] )
                

                for eyePoint in rightEyePoints:
                     for irisPoint in rightIrisPoints:
                          writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[eyePoint].z, face_landmark.landmark[irisPoint].x, face_landmark.landmark[irisPoint].y, face_landmark.landmark[irisPoint].z )] )
                for eyePoint in leftEyePoints:
                     for irisPoint in leftIrisPoints:
                          writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[eyePoint].z, face_landmark.landmark[irisPoint].x, face_landmark.landmark[irisPoint].y,  face_landmark.landmark[irisPoint].z)] )
                

               #  for eyePoint in rightEyePoints:
               #       for facePoint in roundedFacePoints:
               #            writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[eyePoint].z, face_landmark.landmark[facePoint].x, face_landmark.landmark[facePoint].y, face_landmark.landmark[facePoint].z )] )
               #  for eyePoint in leftEyePoints:
               #       for facePoint in roundedFacePoints:
               #            writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[eyePoint].z, face_landmark.landmark[facePoint].x, face_landmark.landmark[facePoint].y,  face_landmark.landmark[facePoint].z)] )

                
            
            
            
            
            # for point in roundedFacePoints:
            #     x = int(face_landmark.landmark[point].x * width)
            #     y = int(face_landmark.landmark[point].y * height)
            #     image = cv2.circle(image, (x,y), 1, (255, 255, 255), 3)
            # cv2.imshow(f"{point}", image)
            # cv2.waitKey(0)
    return image

def test_realtime(image, result):
    
    model = tf.keras.models.load_model(f'iris.h5')

    image.flags.writeable = True
    if result.multi_face_landmarks:
        for face_landmark in result.multi_face_landmarks:
            height, width, _ = image.shape
            with open(f'test.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                
                for point in rightIrisPoints:
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0, 0.5, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0.5, 0, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 1, 0.5, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0.5, 1, 0)] )
                
                for point in rightIrisPoints:
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0, 0.5, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0.5, 0, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 1, 0.5, 0)] )
                    writer.writerow( [euclideanDistance( face_landmark.landmark[point].x, face_landmark.landmark[point].y, face_landmark.landmark[point].z, 0.5, 1, 0)] )
                

                for eyePoint in rightEyePoints:
                     for irisPoint in rightIrisPoints:
                          writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[eyePoint].z, face_landmark.landmark[irisPoint].x, face_landmark.landmark[irisPoint].y, face_landmark.landmark[irisPoint].z )] )
                for eyePoint in leftEyePoints:
                     for irisPoint in leftIrisPoints:
                          writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[eyePoint].z, face_landmark.landmark[irisPoint].x, face_landmark.landmark[irisPoint].y,  face_landmark.landmark[irisPoint].z)] )
               
               

               #  for eyePoint in rightEyePoints:
               #       for facePoint in roundedFacePoints:
               #            writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[eyePoint].z, face_landmark.landmark[facePoint].x, face_landmark.landmark[facePoint].y, face_landmark.landmark[facePoint].z )] )
               #  for eyePoint in leftEyePoints:
               #       for facePoint in roundedFacePoints:
               #            writer.writerow( [euclideanDistance( face_landmark.landmark[eyePoint].x, face_landmark.landmark[eyePoint].y, face_landmark.landmark[eyePoint].z, face_landmark.landmark[facePoint].x, face_landmark.landmark[facePoint].y,  face_landmark.landmark[facePoint].z)] )

    data = []
    directory = f"test.csv"   
    f = os.path.join(directory)                  
    data = pd.read_csv(f'{f}', header=None)
    data = np.array(data)
    res = model.predict(np.expand_dims(data, axis=0))[0]
    print(f"you looked at {np.argmax(res)}")
    # return image

def tryPoints(image, result, label):
    image.flags.writeable = True
    if result.multi_face_landmarks:
        for face_landmark in result.multi_face_landmarks:
            height, width, _ = image.shape
            
            # for point in leftIrisPoints:
            point = leftIrisPoints[0]    
            x = int(face_landmark.landmark[point].x * width)
            y = int(face_landmark.landmark[point].y * height)
            image = cv2.circle(image, (x,y), 1, (255, 255, 255), 3)
            cv2.imshow(f"x: {face_landmark.landmark[point].x}, y: {face_landmark.landmark[point].y} , z: {face_landmark.landmark[point].z}", image)
            print("=======================================================")
            print(f": {face_landmark.landmark[point].z}")
            print("=======================================================")
            cv2.waitKey(0)
                
    return image

def click(label):
    
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    result, landmarks = get_landmark(image)
    
    tryPoints(image, result, "0")
    
    ###################THIS FOR TESTING###################
    # test_realtime(image, result)

    ###################THIS FOR COLLECTING DATA###################
    # img = draw_landmarks(image, result, label)



def create_rectangle(frame,name, button, color, click_nu, col, ro):
    rec_name = name
    rec_name= Button(frame, text= button, bg = color, command=lambda:click(click_nu))
    rec_name.grid(column=col, row=ro, sticky='NSEW' )



    

master = Tk()

master.attributes('-fullscreen', True)
master.title("IRIS control")

master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=1)


master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=1)






# rectangle_1 = Button(master, text="button 0", bg='yellow', command= lambda: click(0))
# rectangle_1.grid(column=0,row=0, sticky='NSEW')
create_rectangle(master, 'rectangle_1', 'Button 0', 'yellow',0,0,0)
create_rectangle(master, 'rectangle_2', 'Button 1', 'blue',1,0,1)
create_rectangle(master, 'rectangle_3', 'Button 2', 'red',2,1,0)
create_rectangle(master, 'rectangle_4', 'Button 3', 'green',3,1,1)

# rectangle_2 = Button(master, text="Button 1", bg='blue', command= lambda: click(1))
# rectangle_2.grid(column=0, row=1, sticky="NSEW")

# rectangle_3 = Button(master, text="Button 2", bg='red', command= lambda: click(2))
# rectangle_3.grid(column=1, row=0, sticky="NSEW")

# rectangle_4 = Button(master, text="Button 3", bg='green', command= lambda: click(3))
# rectangle_4.grid(column=1, row=1, sticky="NSEW")



mainloop()
