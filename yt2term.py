import argparse
import shutil
import subprocess
import time

import cv2
import asciify
from PIL import Image
from yt_dlp import YoutubeDL

from modules import cli, audio


# CONSTANTS
#=======================================================================
TARGET_HZ: int = 30
FRAME_DELTA_TIME: float = 1.0 / TARGET_HZ
#=======================================================================


def control_frame_rate(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start
        sleep_time = FRAME_DELTA_TIME - elapsed

        if sleep_time > 0:
            time.sleep(sleep_time)

        return result

    return wrapper


def read_frame(cap: cv2.VideoCapture):
    ret, frame = cap.read()

    if not ret:
        return None

    return frame


def frame_to_ascii(
    frame,
    width: int,
    color: bool
) -> str:

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    pil_image = Image.fromarray(rgb)

    image = asciify.resize_image(pil_image, width)

    return asciify.pixels_to_colored_ascii(
        image,
        color
    )


def render_frame(art: str):
    print("\033[H", end="") # Clear
    print(art, end="", flush=True)


@control_frame_rate
def process_frame(cap, width, color):
    frame = read_frame(cap)

    if frame is None:
        return False

    art = frame_to_ascii(frame, width, color)

    render_frame(art)

    return True


def get_width(args: argparse.Namespace):
    if args.width is not None:
        return args.width

    return shutil.get_terminal_size().columns


def clear_screen():
    print("\033[2J\033[H", end="")


def main():
    args: argparse.Namespace = cli.get_args()
    color = not args.no_color

    ydl_opts = {
        "format": "best[ext=mp4]",
        "quiet": True,
        "no_warnings": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(args.link, download=False)
        stream_url = info["url"]

    cap = cv2.VideoCapture(stream_url)

    audio_process: subprocess.Popen | None = None
    if args.audio:
        audio_process = audio.get_audio_process(stream_url)

    clear_screen()
    try:
        while True:
            width = get_width(args)

            if not process_frame(cap, width, color):
                break

    except KeyboardInterrupt:
        pass

    finally:
        cap.release()
        if audio_process is not None:
            audio_process.kill()


if __name__ == "__main__":
    main()