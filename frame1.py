import cv2
import os

def extract_frames(video_path, output_folder, num_frames=20):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Calculate frame count and interval
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = max(total_frames // num_frames, 1)

    # Initialize frame count
    frame_count = 0
    extracted_frames = 0

    # Loop through each frame in the video
    while True:
        # Set the frame position
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_count)

        # Read the next frame
        success, frame = video_capture.read()

        # If no frame is returned, break the loop
        if not success:
            break

        # Write the frame to disk
        frame_path = f"{output_folder}/frame_{extracted_frames:04d}.jpg"
        cv2.imwrite(frame_path, frame)

        # Increment frame count
        frame_count += frame_interval
        extracted_frames += 1

        # If reached the desired number of frames, break the loop
        if extracted_frames >= num_frames:
            break

    # Release the video capture object
    video_capture.release()


output_base_folder = "frames_data1"

for i in os.listdir("Dataset"):
    video_folder = os.path.splitext(i)[0]  # Get the name of the video without extension
    output_folder_path = os.path.join(output_base_folder, video_folder)
    os.makedirs(output_folder_path, exist_ok=True)  # Create the output folder if it doesn't exist
    for j in os.listdir("Dataset/" + i):
        print("Dataset/" + i + "/" + j)
        extract_frames("Dataset/" + i + "/" + j, output_folder_path, num_frames=20)


