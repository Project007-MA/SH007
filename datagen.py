import cv2
import os

import numpy as np

from save_load import *
t_frame=[]
label=[]
from sklearn.model_selection import train_test_split
def convert_frame(video_path, label_count, num_frames=20, target_size=(300,200)):
    video_capture = cv2.VideoCapture(video_path)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = max(total_frames // num_frames, 1)

    frame_count = 0
    extracted_frames = 0

    while True:
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
        success, frame = video_capture.read()

        if not success:
            break

        # Resize frame to target size
        frame = cv2.resize(frame, target_size)

        t_frame.append(frame)
        label.append(label_count)

        frame_count += frame_interval
        extracted_frames += 1

        if extracted_frames >= num_frames:
            break

    video_capture.release()

# Call convert_frame() with the appropriate parameters
label_count = -1
for folder in os.listdir("Dataset"):
    label_count += 1
    for file_name in os.listdir("Dataset/" + folder):
        video_path = "Dataset/" + folder + "/" + file_name
        convert_frame(video_path, label_count, num_frames=20, target_size=(300, 200))

t_frame=np.array(t_frame)
label=np.array(label)






X_train, X_test, y_train, y_test = train_test_split(t_frame,label, test_size=0.3, random_state=42)

save("X_train",X_train)
save("X_test",X_test)
save("Y_train",y_train)
save("Y_test",y_test)
