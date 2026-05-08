import argparse
import os
import shutil
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

    return parser.parse_args()


def main():
    target_hz = 20
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


if __name__ == "__main__":
    main()