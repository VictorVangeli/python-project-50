from gendiff.diff_builder.find_diff import find_diff
from gendiff.utils import get_formatter, load_file_to_parse


def generate_diff(
    first_file: str, second_file: str, format_name: str = "stylish"
) -> str:
    """
    Generates the difference between two files in the specified format.

    Args:
        first_file (str): The path to the first file.
        second_file (str): The path to the second file.
        format_name (str, optional): The format for the output. Defaults to
        "stylish". Available formats are "stylish", "plain", "json".

    Returns:
        str: A string representing the differences between the two files
        formatted according to the chosen format.
    """
    text_first_file = load_file_to_parse(first_file)
    text_second_file = load_file_to_parse(second_file)

    diff = find_diff(text_first_file, text_second_file)

    formatter = get_formatter(format_name)
    return formatter(diff)
