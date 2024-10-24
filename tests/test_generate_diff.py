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
            "expected_diff_empty.txt",
        ],
    ],
)
def test_generate_diff_plain(file1, file2, expected):
    file_path_1 = get_fixture_path(file1)
    file_path_2 = get_fixture_path(file2)
    expected_result = read_file(get_fixture_path(expected))
    assert generate_diff(file_path_1,
                         file_path_2).strip() == expected_result.strip()

@pytest.mark.parametrize(
    "expected_exception, args",
    [
        (TypeError, get_fixture_path("plain_file_1.json")),
        (
            FileNotFoundError,
            [
                get_fixture_path("plain_file_1.json"),
                get_fixture_path("plain_file.json"),
            ],
        ),
    ],
)
def test_generate_diff_error(expected_exception, args):
    with pytest.raises(expected_exception):
        generate_diff(*args)
