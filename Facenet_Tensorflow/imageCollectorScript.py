import cv2
import os

def FrameCapture(user, count):
    try:
        index = len(os.listdir(f"database/{user}"))
    except:
        index = 0
        os.mkdir(f"database/{user}")
    camera = cv2.VideoCapture(0)

    for i in range(count):
        index += 1

        _, image = camera.read()
        cv2.imshow("captured", image)
        cv2.imwrite(f"database/{user}/{index}.jpg", image)

        if cv2.waitKey(500) & 0xFF == ord('q'):
            break

# Driver Code
if __name__ == '__main__':
    user = input("Please enter your Name:")
    FrameCapture(user, 30)