import pytube
import os
from urllib.error import HTTPError

def download_video(url, file_type):
    """
    This function downloads a YouTube video as MP3 or MP4 file.

    Args:
    url (str): The URL of the YouTube video to download.
    file_type (str): The file type to download. Either "mp3" or "mp4".

    Returns:
    None
    """
    try:
        yt = pytube.YouTube(url)
        if file_type == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
        elif file_type == "mp4":
            stream = yt.streams.filter(file_extension="mp4").get_highest_resolution()
        else:
            raise ValueError("Invalid file type specified. Must be either 'mp3' or 'mp4'.")

        title = yt.title
        print(f"Downloading {title}...")
        stream.download()
        if file_type == "mp3":
            base, ext = os.path.splitext(stream.default_filename)
            new_filename = base + ".mp3"
            os.rename(stream.default_filename, new_filename)
            print(f"{title} downloaded as {new_filename}")
        elif file_type == "mp4":
            print(f"{title} downloaded as {stream.default_filename}")
    except (pytube.exceptions.PytubeError, HTTPError) as e:
        print(f"Error: {e}")

while True:
    link = input("Youtube url: ")
    chose = input("mp3 or mp4: ")
    download_video(link, chose)
