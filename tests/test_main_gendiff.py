import subprocess

from gendiff import generate_diff
from gendiff.utils import get_fixture_path, read_file


def test_main_gendiff_help():
    expected_result = read_file(
        get_fixture_path("expected_main_gendiff_help.txt")
    )

    result = subprocess.run(
        ["poetry", "run", "gendiff", "-h"], capture_output=True, text=True
    )

    # Получаем вывод и сравниваем с ожидаемым результатом
    assert result.stdout == expected_result


def test_main_gendiff_two_different_files():
    file_path_1 = get_fixture_path('plain_file_1.json')
    file_path_2 = get_fixture_path('plain_file_2.json')
    expected_result = read_file(
        get_fixture_path("expected_diff_main_plain.txt")
    )
    result = subprocess.run(
        ["poetry", "run", "gendiff", file_path_1, file_path_2],
        capture_output=True,
        text=True,
    )

    assert result.stdout.strip() == expected_result.strip()
