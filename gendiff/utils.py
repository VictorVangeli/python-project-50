import json
import yaml
from pathlib import Path


def load_file_to_parse(file_path):
    current_dir = Path(__file__).parent
    file_path = str(file_path)
    if file_path.endswith('.json'):
        with open(current_dir / file_path, "r") as file:
            return json.load(file)
    elif file_path.endswith(('.yaml', '.yml')):
        with open(current_dir / file_path, "r") as file:
            return yaml.safe_load(file)


def read_file(file_path):
    with open(file_path, "r") as f:
        result = f.read()
    return result


def get_fixture_path(file_name):
    current_dir = Path(__file__).parent.parent
    return current_dir / "tests" / "fixtures" / file_name
