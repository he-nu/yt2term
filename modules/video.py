import cv2
from yt_dlp import YoutubeDL


def read_frame(cap: cv2.VideoCapture):
    ret, frame = cap.read()

    if not ret:
        return None

    return frame


def get_stream_url(link: str) -> str:
    ydl_opts = {
        "format": "best[ext=mp4]",
        "quiet": True,
        "no_warnings": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=False)
        stream_url = info["url"]

    return stream_url
