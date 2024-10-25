import pytest
from gendiff.generate_diff import generate_diff
from gendiff.utils import get_fixture_path, read_file


@pytest.mark.parametrize(
    "file1, file2, expected",
    [
        # Проверка различий между двумя JSON файлами (основная задача)
        [
            "plain_file_1.json",
            "plain_file_2.json",
            "expected_diff_main_plain.txt",
        ],
        # Проверка для первого набора одинаковых файлов
        [
            "plain_file_1.json",
            "plain_file_1.json",
            "expected_diff_identical1_plain.txt",
        ],
        # Проверка для второго набора одинаковых файлов
        [
            "plain_file_2.json",
            "plain_file_2.json",
            "expected_diff_identical2_plain.txt",
        ],
        # Проверка различий между пустым файлом и полным
        [
            "file_empty.json",
            "plain_file_1.json",
            "expected_diff_empty_plain.txt",
        ],
        # Проверка различий между двумя YAML файлами (основная задача)
        [
            "plain_file_1.yaml",
            "plain_file_2.yaml",
            "expected_diff_main_plain.txt",
        ],
    ],
)
def test_generate_diff_plain(file1, file2, expected):
    file_path_1 = get_fixture_path(file1, "plain")
    file_path_2 = get_fixture_path(file2, "plain")
    expected_result = read_file(get_fixture_path(expected, "plain"))
    result = generate_diff(
        file_path_1, file_path_2, format_name="plain"
    )
    assert result == expected_result

@pytest.mark.parametrize(
    "expected_exception, args",
    [
        # Если передали только 1 аргумент
        (
            TypeError,
            get_fixture_path("plain_file_1.json", format_name="plain"),
        ),
        # Если передали несуществующую дирректорию для JSON
        (
            FileNotFoundError,
            [
                get_fixture_path("plain_file_1.json", format_name="plain"),
                get_fixture_path("plain_file.json", format_name="plain"),
            ],
        ),
        #
        (
            TypeError,
            get_fixture_path("plain_file_1.yaml", format_name="plain"),
        ),
        # Если передали несуществующую дирректорию для YAML
        (
            FileNotFoundError,
            [
                get_fixture_path("plain_file_1.yaml", format_name="plain"),
                get_fixture_path("plain_file.yaml", format_name="plain"),
            ],
        ),
        # Если передали пустой YAML
        (
            AttributeError,
            [
                get_fixture_path("file_empty.yaml", format_name="plain"),
                get_fixture_path("plain_file_1.yaml", format_name="plain"),
            ],
        ),
    ],
)
def test_generate_diff_error(expected_exception, args):
    with pytest.raises(expected_exception):
        generate_diff(*args)


@pytest.mark.parametrize(
    "file1, file2, expected",
    [
        # Проверка различий между двумя JSON файлами для stylish
        [
            "stylish_file_1.json",
            "stylish_file_2.json",
            "expected_diff_main_stylish.txt",
        ],
        # Проверка для одинаковых JSON файлов (stylish)
        [
            "stylish_file_1.json",
            "stylish_file_1.json",
            "expected_diff_identical1_stylish.txt",
        ],
        # Проверка для одинаковых JSON файлов (stylish)
        [
            "stylish_file_2.json",
            "stylish_file_2.json",
            "expected_diff_identical2_stylish.txt",
        ],
        # Проверка различий между пустым JSON файлом и полным (stylish)
        [
            "file_empty.json",
            "stylish_file_1.json",
            "expected_diff_empty_stylish.txt",
        ],
        # Проверка различий между двумя YAML файлами для stylish
        [
            "stylish_file_1.yaml",
            "stylish_file_2.yaml",
            "expected_diff_main_stylish.txt",
        ],
    ],
)
def test_generate_diff_stylish(file1, file2, expected):
    file_path_1 = get_fixture_path(file1, "stylish")
    file_path_2 = get_fixture_path(file2, "stylish")
    expected_result = read_file(get_fixture_path(expected, "stylish"))

    result = generate_diff(
        file_path_1, file_path_2, format_name="stylish"
    )
    assert result == expected_result
