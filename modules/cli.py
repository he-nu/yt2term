import argparse


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