import mediapipe as mp
import cv2
from tkinter import *
import os

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

def draw_landmarks(image, result):
    image.flags.writeable = True
    if result.multi_face_landmarks:
        for face_landmark in result.multi_face_landmarks:
            # mp_drawing.draw_landmarks(
            #     image=image,
            #     connections=mp_face_mesh.FACEMESH_TESSELATION,
            #     landmark_list=face_landmark,
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style()
            # )
            
            # mp_drawing.draw_landmarks(
            #     image=image,
            #     connections=mp_face_mesh.FACEMESH_CONTOURS,
            #     landmark_list=face_landmark,
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style()
            # )

            # mp_drawing.draw_landmarks(
            #     image=image,
            #     connections=mp_face_mesh.FACEMESH_IRISES,
            #     landmark_list=face_landmark,
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style()
            # )
#7, 
#468 to 477 are iris
            height, width, _ = image.shape
            for i in range(468, 478):
                if i == 7:
                    continue
                pt = face_landmark.landmark[158]
                x = int(pt.x * width)
                y = int(pt.y * height)
                
                cv2.circle(image, (x, y), 3, (100, 100, 0))
            
            
            # for face_landmark in mp_face_mesh.FACEMESH_IRISES:
            #     print(face_landmark)
            #     # pt = face_landmark.landmark
            #     x = int(face_landmark[0])
            #     y = int(face_landmark[1])
                
            #     cv2.circle(image, (x, y), 3, (100, 100, 0))
            
            return image





def click1():
    cam = cv2.VideoCapture(0)
    # reading the input using the camera
    result, image = cam.read()
    cv2.imwrite(os.path.join(os.path.expanduser('~'),'Downloads','Button1.jpg'), image)
    result, landmarks = get_landmark(image)
    img = draw_landmarks(image, result)
    cv2.imshow("test", img)
    cv2.waitKey(0)


























# creating main tkinter window/toplevel
master = Tk()

master.attributes('-fullscreen', True)
master.title("Geeks For Geeks")


master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=1)

master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=1)

rectangle_1 = Button(master, text="button1", bg='yellow', command=click1)
rectangle_1.grid(column=0,row=0, sticky='WENS')

rectangle_2 = Button(master, text="Button 2", bg='blue')
rectangle_2.grid(column=0, row=1, sticky="NSEW")

rectangle_3 = Button(master, text="Button 3", bg='red')
rectangle_3.grid(column=1, row=0, sticky="NSEW")

rectangle_4 = Button(master, text="Button 4", bg='green')
rectangle_4.grid(column=1, row=1, sticky="NSEW")


# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()