import cv2
import numpy as np
# from train import getModel
# from globalModule import *
from Gestures.globalModule.globalModule import *

import tensorflow as tf
from tensorflow.keras.models import load_model

# sequence = []
# sentence = []
# predictions = []
# threshold = 0.5

model = tf.keras.models.load_model(f'{modelPath}/RNN/test.h5')

# model = getModel()
# model.load_weights("model.h5")



colors = [(245,117,16), (117,245,16), (16,117,245)]

def prob_viz(res, actions, input_frame, colors):
    output_frame = input_frame.copy()
    # for num, prob in enumerate(res):
    #     cv2.rectangle(output_frame, (0,60+num*40), (int(prob*100), 90+num*40), colors[num], -1)
    #     cv2.putText(output_frame, actions[num], (0, 85+num*40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
    return output_frame




def main1():

    sequence = []
    sentence = []
    predictions = []
    threshold = 0.5
    cap = cv2.VideoCapture(9)

    # Set mediapipe model 
    with mpHolistics.Holistic(min_detection_confidence=0.8, min_tracking_confidence=0.8) as holistic:
        while cap.isOpened():

            # Read feed
            ret, frame = cap.read()

            # Make detections
            results = mediapipeDetection(frame, holistic)
            # print(results)
            
            # Draw landmarks
            drawLandmarks(frame, results)
            
            # 2. Prediction logic
            keypoints = getKeyPoints(results)
            sequence.append(keypoints)
            sequence = sequence[-30:]
            
            if len(sequence) == 30:
                res = model.predict(np.expand_dims(sequence, axis=0))[0]
                print(actions[np.argmax(res)])
                predictions.append(np.argmax(res))
                
                
            #3. Viz logic
                if np.unique(predictions[-10:])[0]==np.argmax(res): 
                    if res[np.argmax(res)] > threshold: 
                        
                        if len(sentence) > 0: 
                            if actions[np.argmax(res)] != sentence[-1]:
                                sentence.append(actions[np.argmax(res)])
                        else:
                            sentence.append(actions[np.argmax(res)])

                if len(sentence) > 5: 
                    sentence = sentence[-5:]

                # Viz probabilities
                frame = prob_viz(res, actions, frame, colors)
                
            cv2.rectangle(frame, (0,0), (640, 40), (300, 0, 16), -1)
            cv2.putText(frame, str(sentence), (3,30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
            # Show to screen
            cv2.imshow('OpenCV Feed', frame)

            # Break gracefully
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

def main(frames):

    model = load_model(f'{modelPath}/RNN/test.h5')

    print("reached")

    colors = [(245,117,16), (117,245,16), (16,117,245)]

    sequence = []
    sentence = []
    predictions = []
    threshold = 0.5    

    

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
            sequence = sequence[-30:]
            


            if len(sequence) == 30:
                res = model.predict(np.expand_dims(sequence, axis=0))[0]
                print(actions[np.argmax(res)])
                predictions.append(np.argmax(res))
                
                
            #3. Viz logic
                # if np.unique(predictions[-10:])[0]==np.argmax(res): 
                #     if res[np.argmax(res)] > threshold: 
                        
                #         if len(sentence) > 0: 
                #             if actions[np.argmax(res)] != sentence[-1]:
                #                 sentence.append(actions[np.argmax(res)])
                #         else:
                #             sentence.append(actions[np.argmax(res)])

            #     if len(sentence) > 5: 
            #         sentence = sentence[-5:]

            #     # Viz probabilities
            #     frame = prob_viz(res, actions, frame, colors)
                
            # cv2.rectangle(frame, (0,0), (640, 40), (300, 0, 16), -1)
            # cv2.putText(frame, str(sentence), (3,30), 
            #             cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
            # Show to screen
            # cv2.imshow('OpenCV Feed', frame)

            # Break gracefully
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # cv2.destroyAllWindows()

    return



# main1()