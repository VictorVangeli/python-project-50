# !/usr/bin/env python3
"""Main script of gendiff."""
from gendiff.cli.cli import parse_arguments


def main() -> None:
    """Run gendiff to find and print differences between two files."""
    parse_arguments()


if __name__ == "__main__":
    main()
