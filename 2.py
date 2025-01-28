from moviepy.video.io.VideoFileClip import VideoFileClip

# Load the video
clip = VideoFileClip("Dataset/Adi Reddy s 100 Years Old Bungalow Tour  Home Tour  2024 Ap Elections  Kavitha Naga Vlogs.mp4")

# Define the time range to cut (in seconds)
start_time = 1596
end_time = 1606

# Cut the video
cut_clip = clip.subclip(start_time, end_time)

# Save the cut video
cut_clip.write_videofile("7.mp4")
