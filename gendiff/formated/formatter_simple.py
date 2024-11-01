from typing import Any, Callable, Dict, List

from gendiff.const import INDENT_DICT


def format_diff_simple(diff: List[Dict[str, Any]]) -> str:
    """
    Formats the structured diff data into a simple plain text format.

    Args:
        diff (List[Dict[str, Any]]): The structured diff data.

    Returns:
        str: A formatted string representing the diff in a simple format.
    """
    to_diff = []
    formatter_functions = formatters_simple()

    for info in diff:
        type_ = info["type"]
        formatted_text = formatter_functions[type_](info)

        if isinstance(formatted_text, list):
            to_diff.extend(formatted_text)
        else:
            to_diff.append(formatted_text)

    return "\n".join(to_diff)


def formatters_simple() -> Dict[str, Callable[[Dict[str, Any]], str]]:
    indent = INDENT_DICT.get("indent_size_for_simple")

    return {
        "added": lambda info: f"{indent}+ {info['key']}: {info['new_value']}",
        "removed": lambda info: f"{indent}- {info['key']}: {info['old_value']}",
        "changed": lambda info: [
            f"{indent}- {info['key']}: {info['old_value']}",
            f"{indent}+ {info['key']}: {info['new_value']}",
        ],
        "unchanged": lambda info: f"{indent}  {info['key']}: {info['value']}",
    }
