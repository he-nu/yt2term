import platform
import shutil
import subprocess
import time


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
