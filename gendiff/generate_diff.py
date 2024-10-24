from gendiff.find_diff import find_diff
from gendiff.utils import load_json


def generate_diff(first_file, second_file):
    text_first_file = load_json(first_file)
    text_second_file = load_json(second_file)

    diff = find_diff(text_first_file, text_second_file)

    return diff
