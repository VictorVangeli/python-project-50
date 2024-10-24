import json
from pathlib import Path


def load_json(file_path):
    current_dir = Path(__file__).parent
    with open(current_dir / file_path, "r") as file:
        return json.load(file)


def read_file(file_path):
    with open(file_path, "r") as f:
        result = f.read()
    return result


def get_fixture_path(file_name):
    current_dir = Path(__file__).parent
    return current_dir / "fixtures" / file_name
