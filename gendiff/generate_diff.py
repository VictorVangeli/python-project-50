from gendiff.find_diff import find_diff
from gendiff.formatter import get_formatter
from gendiff.utils import load_file_to_parse


def generate_diff(first_file, second_file, format_name='stylish'):
    # Загружаем файлы
    text_first_file = load_file_to_parse(first_file)
    text_second_file = load_file_to_parse(second_file)

    # Находим отличия
    diff = find_diff(text_first_file, text_second_file)

    # Получаем форматтер и форматируем результат
    formatter = get_formatter(format_name)
    return formatter(diff)
