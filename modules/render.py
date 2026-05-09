import time

import cv2
import asciify
from PIL import Image


# CONSTANTS
#=======================================================================
TARGET_HZ: int = 30
FRAME_DELTA_TIME: float = 1.0 / TARGET_HZ
#=======================================================================


def clear_screen():
    print("\033[2J\033[H", end="")


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
def process_frame(frame, width, color):
    if frame is None:
        return False

    art = frame_to_ascii(frame, width, color)

    render_frame(art)

    return True
