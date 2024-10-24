import os

import pytest
from gendiff.generate_diff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "fixtures", file_name)


def read_fixtures(file_path):
    with open(file_path, "r") as f:
        result = f.read()
    return result


def test_generate_diff_plain_main():
    file_path_1 = get_fixture_path("plain_file_1.json")
    file_path_2 = get_fixture_path("plain_file_2.json")
    excepted_result = read_fixtures("excepted_diff_main_plain.txt")
    assert generate_diff(file_path_1, file_path_2) == excepted_result


def test_generate_diff_plain_identical1():
    file_path_1 = get_fixture_path("plain_file_1.json")
    excepted_result = read_fixtures("excepted_diff_identical1_plain.txt")
    assert generate_diff(file_path_1, file_path_1) == excepted_result


def test_generate_diff_identical2():
    file_path_2 = get_fixture_path("plain_file_2.json")
    excepted_result = read_fixtures("excepted_diff_identical2_plain.txt")
    assert generate_diff(file_path_2, file_path_2) == excepted_result


def test_generate_diff_empty():
    file_path_1 = get_fixture_path("file_empty.json")
    file_path_2 = get_fixture_path("plain_file_1.json")
    excepted_result = read_fixtures("excepted_diff_empty_plain.txt")
    assert generate_diff(file_path_1, file_path_2) == excepted_result


@pytest.mark.parametrize(
    "excepted_exception, args",
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
def test_generate_diff_error(excepted_exception, args):
    with pytest.raises(excepted_exception):
        generate_diff(*args)
