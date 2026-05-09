import argparse
import shutil


def get_args() -> argparse.Namespace:
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


def get_width(args: argparse.Namespace) -> int:
    if args.width is not None:
        return args.width

    return shutil.get_terminal_size().columns