from gendiff.find_diff import find_diff
from gendiff.utils import load_file_to_parse


def generate_diff(first_file, second_file):
    text_first_file = load_file_to_parse(first_file)
    text_second_file = load_file_to_parse(second_file)

    diff = find_diff(text_first_file, text_second_file)

    return diff
