import json
from typing import Any


def format_diff_json(diff: Any) -> str:
    """
    Formats the given diff into a JSON string with indentation.

    Args:
        diff (Any): The difference data to be formatted as JSON.

    Returns:
        str: A JSON-formatted string with an indentation of 4 spaces.
    """
    return json.dumps(diff, indent=4)
