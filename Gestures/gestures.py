from tensorflow.keras.models import load_model as tf_load_model
import numpy as np
import cv2
from globalModule.globalModule import *


class gestures():
    def __init__(self) -> None:

        gestures_dict = {
        'click': 0,
        'swipe up': 1,
        'volume up': 2,
        'close': 3,
        'pause&play': 4,
        'anothingg': 5,
        }
       
        # self.model = tf_load_model(modelDir)
        self.model = tf_load_model(f'{modelPath}/RNN/test.h5')

        self.colors = [(245,117,16), (117,245,16), (16,117,245)]
        
        self.predictions = []
    
    def predict(self, frames):
        sequence = []
        # Set mediapipe model 
        with mpHolistics.Holistic(min_detection_confidence=0.8, min_tracking_confidence=0.8) as holistic:
            for frame in frames:
                # Make detections
        
                results = mediapipeDetection(frame, holistic)
                # print(results)
                
                # Draw landmarks
                drawLandmarks(frame, results)

                # 2. Prediction logic
                keypoints = getKeyPoints(results)
                sequence.append(keypoints)
                # sequence = sequence[-30:]
                
                if len(sequence) == 30:
                    res = self.model.predict(np.expand_dims(sequence, axis=0))[0]
                    print(actions[np.argmax(res)])
                    self.predictions.append(np.argmax(res))
                          
         


