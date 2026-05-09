import argparse
import subprocess

import cv2

from modules import (
    cli,
    audio,
    video,
    render,
)


def main():
    args: argparse.Namespace = cli.get_args()
    color = not args.no_color

    stream_url = video.get_stream_url(link=args.link)

    cap = cv2.VideoCapture(stream_url)

    audio_process: subprocess.Popen | None = None
    if args.audio:
        audio_process = audio.get_audio_process(stream_url)

    render.clear_screen()
    try:
        while True:
            width = cli.get_width(args)
            frame = video.read_frame(cap)

            if not render.process_frame(frame, width, color):
                break

    except KeyboardInterrupt:
        pass

    finally:
        cap.release()
        if audio_process is not None:
            audio_process.kill()


if __name__ == "__main__":
    main()