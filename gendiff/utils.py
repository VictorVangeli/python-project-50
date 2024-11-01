import json
from pathlib import Path

import yaml
from gendiff.formated.formatted_json import format_diff_json
from gendiff.formated.formatted_plain import format_diff_plain
from gendiff.formated.formatter_simple import format_diff_simple
from gendiff.formated.formatter_stylish import format_diff_stylish


def get_formatter(format_name: str):
    """
    Returns the appropriate formatter function based on the format_name.

    Args:
        format_name (str): The name of the output format (e.g., stylish, plain).

    Returns:
        Callable: The formatting function corresponding to the format_name.
    """
    format_name_dict = {
        "simple": format_diff_simple,
        "stylish": format_diff_stylish,
        "plain": format_diff_plain,
        "json": format_diff_json,
    }
    return format_name_dict.get(format_name)


def load_file_to_parse(file_path: str):
    """
    Loads and parses the contents of a file based on its extension
    (JSON or YAML).

    Args:
        file_path (str): The path to the file to be loaded.

    Returns:
        dict: The parsed contents of the file as a dictionary.
    """
    current_dir = Path(__file__).parent
    file_path = str(file_path)
    if file_path.endswith(".json"):
        with open(current_dir / file_path, "r") as file:
            return json.load(file)
    elif file_path.endswith((".yaml", ".yml")):
        with open(current_dir / file_path, "r") as file:
            return yaml.safe_load(file)


def read_file(file_path: str) -> str:
    """
    Reads the contents of a file.

    Args:
        file_path (Path): The path to the file to read.

    Returns:
        str: The contents of the file as a string.
    """
    with open(file_path, "r") as f:
        result = f.read()
    return result


def get_fixture_path(file_name: str, format_name: str) -> str:
    """
    Constructs the path to a test fixture based on the file name and format.

    Args:
        file_name (str): The name of the fixture file (e.g., expected_diff.txt).
        format_name (str): The format name (e.g., stylish, plain).

    Returns:
        Path: The constructed path to the fixture file.
    """
    current_dir = Path(__file__).parent.parent
    file_name = file_name.lower()

    match format_name:
        case "plain" | "stylish" | "simple" | "json":
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
        case "other":
            if file_name.endswith(".txt"):
                # fmt: off
                return current_dir / "tests" / "fixtures" / file_name
                # fmt: on
