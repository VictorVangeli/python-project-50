# !/usr/bin/env python3
"""Main script of gendiff."""
from gendiff import generate_diff
from gendiff.cli.cli import get_args


def main() -> None:
    """Run gendiff to find and print differences between two files."""
    args = get_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
