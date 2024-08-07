import os
import yt_dlp

cur_dir = os.getcwd()

def download_video(link, id):
    youtube_dl_options = {
        "format": "b",  # This will select the specific resolution typed here
        "outtmpl": os.path.join(cur_dir, f"{id}.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])

download_video('https://youtu.be/fA5Sby1F2hg?si=q_2pJAdsMiaCnUlc', 'video_filename')