from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Adjust this to specify allowed methods
    allow_headers=["*"],  # Adjust this to specify allowed headers
)

# Define a model for the incoming request
class VideoRequest(BaseModel):
    url: str
    filename: str

def download_video(link: str, filename: str, save_path: str):
    youtube_dl_options = {
        "format": "bestvideo+bestaudio/best",  # Use the best available video and audio formats
        "outtmpl": os.path.join(save_path, f"{filename}.mp4")
    }
    try:
        with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
            ydl.download([link])
        return {"status": "success", "message": "Download completed!"}
    except yt_dlp.DownloadError as e:
        raise HTTPException(status_code=400, detail=f"Download error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.post("/download/")
async def download_video_endpoint(request: VideoRequest):
    save_path = os.path.expanduser("~/Downloads")  # Save video to user's Downloads directory
    result = download_video(request.url, request.filename, save_path)
    return result
