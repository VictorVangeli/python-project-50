import argparse


def get_args():
    """
    Parse arguments for gendiff.

    Returns:
        args.first_file: str
        args.second_file: str
        args.format: str
    """
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration "
        "files and "
        "shows a difference.",
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        "-f",
        "--format",
        default="stylish",
        help=(
            "set format of output (default: stylish, "
            "variables: plain, simple, json)"
        ),
    )
    return parser.parse_args()
