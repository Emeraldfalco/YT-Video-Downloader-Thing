import os
from yt_dlp import YoutubeDL

def download_video(url, output_path='downloads'):
    os.makedirs(output_path, exist_ok=True)
    options = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
    }
    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        return info

def download_subtitles(url, output_path='downloads'):
    os.makedirs(output_path, exist_ok=True)
    options = {
        'writesubtitles': True,
        'subtitleslangs': ['en'],  # Specify languages
        'skip_download': True,    # Do not download the video
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        return info
