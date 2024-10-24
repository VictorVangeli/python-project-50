import json

from pathlib import Path


def load_json(file_path):
    current_dir = Path(__file__).parent
    with open(current_dir / file_path, "r") as file:
        return json.load(file)
