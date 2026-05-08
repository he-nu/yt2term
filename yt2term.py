import argparse
import os
import platform
import shutil
import subprocess
import time

import cv2
import asciify
from PIL import Image
from yt_dlp import YoutubeDL


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "link",
        type=str,
        nargs="?",
        default="https://www.youtube.com/watch?v=IxX_QHay02M",
        help="YouTube/video link"
    )

    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable color output"
    )

    parser.add_argument(
        "--width",
        type=int,
        help="ASCII width"
    )

    parser.add_argument(
    "--audio",
    action="store_true",
    help="Enable audio playback (requires ffplay)"
)

    return parser.parse_args()


def ensure_ffplay():
    if shutil.which("ffplay") is not None:
        return True

    print("ffplay not found.")

    answer = input(
        "Would you like to install FFmpeg? (y/n): "
    ).strip().lower()

    if answer != "y":
        return False

    system = platform.system()

    try:
        if system == "Windows":
            subprocess.run(
                ["winget", "install", "Gyan.FFmpeg"],
                check=True
            )

        elif system == "Darwin":
            subprocess.run(
                ["brew", "install", "ffmpeg"],
                check=True
            )

        elif system == "Linux":
            subprocess.run(
                ["sudo", "apt", "install", "-y", "ffmpeg"],
                check=True
            )

        else:
            print("Unsupported operating system.")
            return False

    except Exception as e:
        print(f"Installation failed: {e}")
        return False

    return shutil.which("ffplay") is not None


def get_audio_process(stream_url: str):
    if not ensure_ffplay():
        print("Resuming play without audio.")
        time.sleep(2)
        return None

    return subprocess.Popen(
        [
            "ffplay",
            "-nodisp",
            "-autoexit",
            "-loglevel",
            "quiet",
            stream_url
        ]
    )


def main():
    target_hz = 30
    dt = 1.0 / target_hz

    args = get_args()

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
        audio_process = get_audio_process(stream_url)

    try:
        while True:
            start = time.perf_counter()
            ret, frame = cap.read()

            if not ret:
                break

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            pil_image = Image.fromarray(rgb)

            if args.width is not None:
                width = args.width
            else:
                width = shutil.get_terminal_size().columns

            image = asciify.resize_image(pil_image, width)

            art = asciify.pixels_to_colored_ascii(
                image,
                not args.no_color
            )

            os.system("cls" if os.name == "nt" else "clear")

            print(art)

            elapsed = time.perf_counter() - start
            sleep_time = dt - elapsed

            if sleep_time > 0:
                time.sleep(sleep_time)

    except KeyboardInterrupt:
        cap.release()

    finally:
        cap.release()
        if audio_process is not None:
            audio_process.kill()


if __name__ == "__main__":
    main()