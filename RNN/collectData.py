from globalModule.globalModule import * 

if __name__ == "__main__":

    for action in actions:
        for sequence in range(noSequences):
            try:
                os.makedirs(os.path.join(gesturesDataPath, action, str(sequence)))
            except Exception as e:
                print("error happened: ", e)

    cap = cv2.VideoCapture(0)

    with mpHolistics.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        
        for action in actions:
            # Loop through sequences aka videos
            for sequence in range(noSequences):
                # Loop through video length aka sequence length
                for frame_num in range(sequenceLen):

                    # Read feed
                    ret, frame = cap.read()

                    # Make detections
                    results = mediapipeDetection(frame, holistic)

                    # Draw landmarks
                    drawLandmarks(frame, results)
                    
                    # NEW Apply wait logic
                    if frame_num == 0: 
                        cv2.putText(frame, 'STARTING COLLECTION', (120,200), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                        cv2.putText(frame, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        # Show to screen
                        cv2.imshow('OpenCV Feed', frame)
                        cv2.waitKey(500)
                    else: 
                        cv2.putText(frame, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        # Show to screen
                        cv2.imshow('OpenCV Feed', frame)
                    
                    # NEW Export keypoints
                    keypoints = getKeyPoints(results)
                    npy_path = os.path.join(gesturesDataPath, action, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)

                    # Break gracefully
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                        
    cap.release()
    cv2.destroyAllWindows()