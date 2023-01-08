from sklearn.model_selection import train_test_split
import os
from tensorflow.keras.utils import to_categorical
from collectData import actions, noSequences, sequenceLen, dataPath, gesturesDataPath
import numpy as np


labelMap = {label:num for num, label in enumerate(actions)}

sequences, labels = [], []
print(dataPath)
for action in actions:
    try:
        for sequence in np.array(os.listdir(os.path.join(gesturesDataPath, action))).astype(int):
            window = []
            for frame_num in range(sequenceLen):
                try:
                    res = np.load(os.path.join(gesturesDataPath, action, str(sequence), "{}.npy".format(frame_num)))
                    window.append(res)
                except Exception as e:
                    print(e)
            sequences.append(window)
            labels.append(labelMap[action])
    except Exception as e:
        print(e)
