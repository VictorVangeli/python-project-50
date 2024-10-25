import subprocess
import pytest

from gendiff.utils import get_fixture_path, read_file


def test_main_gendiff_help():
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
            "plain_file_1.json",
            "plain_file_2.json",
            "plain",
            "expected_diff_main_plain.txt",
        ),
        (
            "plain_file_1.yaml",
            "plain_file_2.yaml",
            "plain",
            "expected_diff_main_plain.txt",
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
def test_main_gendiff_formats(file1, file2, format_name, expected_output):
    file_path_1 = get_fixture_path(file1, format_name)
    file_path_2 = get_fixture_path(file2, format_name)
    expected_result = read_file(get_fixture_path(expected_output, format_name))

    result = subprocess.run(
        [
            "poetry",
            "run",
            "gendiff",
            file_path_1,
            file_path_2,
            "-f",
            format_name,
        ],
        capture_output=True,
        text=True,
    )

    assert result.stdout.strip() == expected_result.strip()
