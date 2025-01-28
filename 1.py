from pytube import YouTube


# Function to download a YouTube video
def download_video(url, save_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download(output_path=save_path)
        print("Download completed successfully!")
    except Exception as e:
        print("An error occurred:", str(e))


# Example usage
if __name__ == "__main__":
    video_url = "https://youtu.be/JyCkuN7cCQI?si=lx0hcX1iD20nqbTv"  # Example URL
    save_path = "Dataset"  # Set your desired save path
    download_video(video_url, save_path)
