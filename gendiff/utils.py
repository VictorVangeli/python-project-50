import json
from pathlib import Path

import yaml
from gendiff.formated.formatted_plain import format_diff_plain
from gendiff.formated.formatter_simple import format_diff_simple
from gendiff.formated.formatter_stylish import format_diff_stylish


def get_formatter(format_name):
    match format_name:
        case "simple":
            return format_diff_simple
        case "stylish":
            return format_diff_stylish
        case "plain":
            return format_diff_plain


def load_file_to_parse(file_path):
    current_dir = Path(__file__).parent
    file_path = str(file_path)
    if file_path.endswith(".json"):
        with open(current_dir / file_path, "r") as file:
            return json.load(file)
    elif file_path.endswith((".yaml", ".yml")):
        with open(current_dir / file_path, "r") as file:
            return yaml.safe_load(file)


def read_file(file_path):
    with open(file_path, "r") as f:
        result = f.read()
    return result


def get_fixture_path(file_name, format_name: str):
    current_dir = Path(__file__).parent.parent
    file_name = file_name.lower()

    match format_name:
        case "plain" | "stylish" | "simple":
            match file_name:
                case name if name.endswith(".json"):
                    # fmt: off
                    return (current_dir / "tests" / "fixtures"
                            / format_name.capitalize() / "JSON" / file_name)
                    # fmt: on
                case name if name.endswith((".yaml", ".yml")):
                    # fmt: off
                    return (current_dir / "tests" / "fixtures"
                            / format_name.capitalize() / "YAML" / file_name)
                    # fmt: on
                case name if name.startswith("expected_"):
                    # fmt: off
                    return (current_dir / "tests" / "fixtures"
                            / format_name.capitalize() / "Expected" / file_name)
                    # fmt: on
        case "other":
            if file_name.endswith(".txt"):
                # fmt: off
                return current_dir / "tests" / "fixtures" / file_name
                # fmt: on
