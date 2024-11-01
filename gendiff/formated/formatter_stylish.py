from typing import Any, Callable, Dict

from gendiff.const import INDENT_SIZE
from gendiff.formated.formatted_methods import (
    format_added,
    format_changed,
    format_removed,
    format_unchanged,
)


def format_diff_stylish(diff: list, depth: int = 1) -> str:
    """
    Formats a diff in the 'stylish' format.

    Args:
        diff (list): The diff structure to be formatted.
        depth (int): Current nesting depth.

    Returns:
        str: Formatted diff string in the 'stylish' format.
    """
    current_indent = " " * (depth * INDENT_SIZE - 2)
    result = ["{"]

    formatter_functions = formatters_stylish(current_indent, depth)

    for node in diff:
        type_ = node["type"]
        if type_ in formatter_functions:
            formatted_text = formatter_functions[type_](node)
            if isinstance(formatted_text, list):
                result.extend(formatted_text)
            else:
                result.append(formatted_text)

    result.append(f"{' ' * ((depth - 1) * INDENT_SIZE)}}}")
    return "\n".join(result)


def format_nested(key: str, children: list, indent: str, depth: int) -> str:
    """
    Formats a string for a nested element.

    Args:
        key (str): The element's key.
        children (list): Nested children elements.
        indent (str): Current indentation level.
        depth (int): Depth of the nested structure.

    Returns:
        str: Formatted string representing the nested element.
    """
    nested_diff = format_diff_stylish(children, depth + 1)
    return f"{indent}  {key}: {nested_diff}"


def formatters_stylish(
    current_indent: str, depth: int
) -> Dict[str, Callable[[Dict[str, Any]], str]]:
    """
    Returns a dictionary with formatting functions for each type of diff change.

    Args:
        current_indent (str): The current indentation level.
        depth (int): The current depth for nested structures.

    Returns:
        Dict[str, Callable[[Dict[str, Any]], str]]: Dictionary of format
        functions.
    """
    templates = {
        "added": lambda node: format_added(
            node["key"],
            format_value_stylish(node["new_value"], depth),
            current_indent,
        ),
        "removed": lambda node: format_removed(
            node["key"],
            format_value_stylish(node["old_value"], depth),
            current_indent,
        ),
        "changed": lambda node: format_changed(
            node["key"],
            format_value_stylish(node["old_value"], depth),
            format_value_stylish(node["new_value"], depth),
            current_indent,
        ),
        "unchanged": lambda node: format_unchanged(
            node["key"],
            format_value_stylish(node["value"], depth),
            current_indent,
        ),
        "nested": lambda node: format_nested(
            node["key"], node["children"], current_indent, depth
        ),
    }
    return templates


def format_value_stylish(value: any, depth: int) -> str:
    """
    Formats a value for the 'stylish' format.

    Args:
        value (any): The value to be formatted.
        depth (int): Current nesting depth.

    Returns:
        str: Formatted value as a string.
    """
    match value:
        case bool():
            return str(value).lower()
        case None:
            return "null"
        case int():
            return str(value)
        case dict():
            return format_dict(value, depth)
        case _:
            return str(value)


def format_dict(value: dict, depth: int) -> str:
    """
    Formats a dictionary as a string for the 'stylish' format.

    Args:
        value (dict): Dictionary to be formatted.
        depth (int): Current nesting depth.

    Returns:
        str: Formatted string representation of the dictionary.
    """
    lines = []
    current_indent = " " * (depth * INDENT_SIZE)
    child_indent = " " * ((depth + 1) * INDENT_SIZE)

    for key, val in value.items():
        formatted_val = format_value_stylish(val, depth + 1)
        lines.append(f"{child_indent}{key}: {formatted_val}")

    closing_bracket_indent = current_indent
    return "{\n" + "\n".join(lines) + f"\n{closing_bracket_indent}}}"  # noqa
