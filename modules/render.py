import time
from typing import Callable

import cv2
import asciify
import numpy as np
from PIL import Image


# CONSTANTS
#=======================================================================
TARGET_HZ: int = 30
FRAME_DELTA_TIME: float = 1.0 / TARGET_HZ
#=======================================================================


def clear_screen() -> None:
    print("\033[2J\033[H", end="")


def control_frame_rate(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start: float = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed: float = time.perf_counter() - start
        sleep_time: float = FRAME_DELTA_TIME - elapsed

        if sleep_time > 0:
            time.sleep(sleep_time)

        return result

    return wrapper


def frame_to_ascii(
    frame: np.ndarray,
    width: int,
    color: bool
) -> str:

    rgb: np.ndarray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    pil_image: Image.Image = Image.fromarray(rgb)

    image = asciify.resize_image(pil_image, width)

    return asciify.pixels_to_colored_ascii(
        image,
        color
    )


def render_frame(art: str) -> None:
    print("\033[H", end="") # Clear
    print(art, end="", flush=True)


@control_frame_rate
def process_frame(
    frame: np.ndarray | None,
    width: int,
    color: bool
) -> bool:

    if frame is None:
        return False

    art: str = frame_to_ascii(frame, width, color)

    render_frame(art)

    return True
