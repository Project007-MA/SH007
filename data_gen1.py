import cv2
import numpy as np
import cv2
import os

import numpy as np

from save_load import *
# Initialize lists
t_frame = []
label = []

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

# Convert lists to NumPy arrays
t_frame_array = np.array(t_frame)
label_array = np.array(label)
