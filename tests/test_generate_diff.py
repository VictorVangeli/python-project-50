from typing import Type

import pytest
from gendiff.diff_builder.generate_diff import generate_diff
from gendiff.utils import get_fixture_path, read_file


@pytest.mark.parametrize(
    "file1, file2, expected",
    [
        # Проверка различий между двумя JSON файлами (основная задача)
        [
            "simple_file_1.json",
            "simple_file_2.json",
            "expected_diff_main_simple.txt",
        ],
        # Проверка для первого набора одинаковых файлов
        [
            "simple_file_1.json",
            "simple_file_1.json",
            "expected_diff_identical1_simple.txt",
        ],
        # Проверка для второго набора одинаковых файлов
        [
            "simple_file_2.json",
            "simple_file_2.json",
            "expected_diff_identical2_simple.txt",
        ],
        # Проверка различий между пустым файлом и полным
        [
            "file_empty.json",
            "simple_file_1.json",
            "expected_diff_empty_simple.txt",
        ],
        # Проверка различий между двумя YAML файлами (основная задача)
        [
            "simple_file_1.yaml",
            "simple_file_2.yaml",
            "expected_diff_main_simple.txt",
        ],
    ],
)
def test_generate_diff_simple(file1: str, file2: str, expected: str) -> None:
    """
    Test gendiff output in simple format for different file pairs.

    Args:
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.
        expected (str): Path to the expected output file.
    """
    file_path_1 = get_fixture_path(file1, "simple")
    file_path_2 = get_fixture_path(file2, "simple")
    expected_result = read_file(get_fixture_path(expected, "simple"))
    result = generate_diff(file_path_1, file_path_2, format_name="simple")
    assert result == expected_result


@pytest.mark.parametrize(
    "expected_exception, args",
    [
        # Если передали только 1 аргумент
        (
            TypeError,
            get_fixture_path("simple_file_1.json", format_name="simple"),
        ),
        # Если передали несуществующую дирректорию для JSON
        (
            FileNotFoundError,
            [
                get_fixture_path("simple_file_1.json", format_name="simple"),
                get_fixture_path("simple_file.json", format_name="simple"),
            ],
        ),
        #
        (
            TypeError,
            get_fixture_path("simple_file_1.yaml", format_name="simple"),
        ),
        # Если передали несуществующую дирректорию для YAML
        (
            FileNotFoundError,
            [
                get_fixture_path("simple_file_1.yaml", format_name="simple"),
                get_fixture_path("simple_file.yaml", format_name="simple"),
            ],
        ),
        # Если передали пустой YAML
        (
            AttributeError,
            [
                get_fixture_path("file_empty.yaml", format_name="simple"),
                get_fixture_path("simple_file_1.yaml", format_name="simple"),
            ],
        ),
    ],
)
def test_generate_diff_error(expected_exception, args: list[str]) -> None:
    """
    Test error cases when invalid file paths or arguments are provided.

    Args:
        expected_exception: The expected exception.
        args (list): List of arguments to pass to generate_diff.

    Raises:
        pytest.raises: Confirms that the expected exception is raised.
    """
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
def test_generate_diff_stylish(file1: str, file2: str, expected: str) -> None:
    """
    Test gendiff output in stylish format for different file pairs.

    Args:
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.
        expected (str): Path to the expected output file.
    """
    file_path_1 = get_fixture_path(file1, "stylish")
    file_path_2 = get_fixture_path(file2, "stylish")
    expected_result = read_file(get_fixture_path(expected, "stylish"))

    result = generate_diff(file_path_1, file_path_2, format_name="stylish")
    assert result == expected_result


@pytest.mark.parametrize(
    "file1, file2, expected",
    [
        # Проверка различий между двумя JSON файлами для plain
        [
            "plain_file_1.json",
            "plain_file_2.json",
            "expected_diff_main_plain.txt",
        ],
        # Проверка для одинаковых JSON файлов (plain)
        [
            "plain_file_1.json",
            "plain_file_1.json",
            "expected_diff_identical1_plain.txt",
        ],
        # Проверка для одинаковых JSON файлов (plain)
        [
            "plain_file_2.json",
            "plain_file_2.json",
            "expected_diff_identical2_plain.txt",
        ],
        # Проверка различий между пустым JSON файлом и полным (plain)
        [
            "file_empty.json",
            "plain_file_1.json",
            "expected_diff_empty_plain.txt",
        ],
        # Проверка различий между двумя YAML файлами для plain
        [
            "plain_file_1.yaml",
            "plain_file_2.yaml",
            "expected_diff_main_plain.txt",
        ],
    ],
)
def test_generate_diff_plain(file1: str, file2: str, expected: str) -> None:
    """
    Test gendiff output in plain format for different file pairs.

    Args:
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.
        expected (str): Path to the expected output file.
    """
    file_path_1 = get_fixture_path(file1, "plain")
    file_path_2 = get_fixture_path(file2, "plain")
    expected_result = read_file(get_fixture_path(expected, "plain"))

    result = generate_diff(file_path_1, file_path_2, format_name="plain")
    assert result == expected_result


@pytest.mark.parametrize(
    "file1, file2, expected",
    [
        # Проверка различий между двумя TXT файлами для stylish
        [
            "json_file_1.json",
            "json_file_2.json",
            "expected_diff_main_json.txt",
        ],
        # Проверка для одинаковых TXT файлов (stylish)
        [
            "json_file_1.json",
            "json_file_1.json",
            "expected_diff_identical1_json.txt",
        ],
        # Проверка для одинаковых TXT файлов (stylish)
        [
            "json_file_2.json",
            "json_file_2.json",
            "expected_diff_identical2_json.txt",
        ],
        # Проверка различий между пустым TXT файлом и полным (stylish)
        [
            "file_empty.json",
            "json_file_1.json",
            "expected_diff_empty_json.txt",
        ],
        # Проверка различий между двумя YAML файлами для stylish
        [
            "json_file_1.yaml",
            "json_file_2.yaml",
            "expected_diff_main_json.txt",
        ],
    ],
)
def test_generate_diff_json(file1: str, file2: str, expected: str) -> None:
    """
    Test gendiff output in JSON format for different file pairs.

    Args:
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.
        expected (str): Path to the expected output file.
    """
    file_path_1 = get_fixture_path(file1, "json")
    file_path_2 = get_fixture_path(file2, "json")
    expected_result = read_file(get_fixture_path(expected, "json"))

    result = generate_diff(file_path_1, file_path_2, format_name="json")
    assert result == expected_result
