import cv2
import os

def FaceCollector(user, count):
    try:
        index = len(os.listdir(f"train_img/{user}"))
    except:
        index = 0
        
        os.mkdir(f"train_img/{user}")
    camera = cv2.VideoCapture(0)

    for i in range(count):
        index += 1

        _, image = camera.read()
        cv2.imshow("captured", image)
        cv2.imwrite(f"train_img/{user}/{index}.jpg", image)

        if cv2.waitKey(500) & 0xFF == ord('q'):
            break

