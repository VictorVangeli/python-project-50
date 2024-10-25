import subprocess

import pytest
from gendiff.utils import get_fixture_path, read_file


def test_main_gendiff_help() -> None:
    """
    Test the output of the 'gendiff' help command.

    Reads the expected result from a fixture file and compares it with the
    actual output of the 'gendiff -h' command.

    Raises:
        AssertionError: If the actual output does not match the expected result.
    """
    expected_result = read_file(
        get_fixture_path("expected_main_gendiff_help.txt", "other")
    )

    result = subprocess.run(
        ["poetry", "run", "gendiff", "-h"], capture_output=True, text=True
    )

    # Получаем вывод и сравниваем с ожидаемым результатом
    assert result.stdout == expected_result


@pytest.mark.parametrize(
    "file1, file2, format_name, expected_output",
    [
        (
            "simple_file_1.json",
            "simple_file_2.json",
            "simple",
            "expected_diff_main_simple.txt",
        ),
        (
            "simple_file_1.yaml",
            "simple_file_2.yaml",
            "simple",
            "expected_diff_main_simple.txt",
        ),
        (
            "stylish_file_1.json",
            "stylish_file_2.json",
            "stylish",
            "expected_diff_main_stylish.txt",
        ),
        (
            "stylish_file_1.yaml",
            "stylish_file_2.yaml",
            "stylish",
            "expected_diff_main_stylish.txt",
        ),
    ],
)
def test_main_gendiff_formats(
    file1: str, file2: str, format_name: str, expected_output: str
) -> None:
    """
    Test the 'gendiff' command with different file formats.

    Parameters:
        file1 (str): The first file path.
        file2 (str): The second file path.
        format_name (str): The format to be used for the diff output.
        expected_output (str): The expected output result.

    Raises:
        AssertionError: If the actual output does not match the expected result.
    """
    file_path_1 = get_fixture_path(file1, format_name)
    file_path_2 = get_fixture_path(file2, format_name)
    expected_result = read_file(get_fixture_path(expected_output, format_name))

    result = subprocess.run(
        [
            "poetry",
            "run",
            "gendiff",
            str(file_path_1),
            str(file_path_2),
            "-f",
            format_name,
        ],
        capture_output=True,
        text=True,
    )

    assert result.stdout.strip() == expected_result.strip()
