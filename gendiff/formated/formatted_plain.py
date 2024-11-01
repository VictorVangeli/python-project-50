from gendiff.const import (
    TEMPLATE_ADDED,
    TEMPLATE_CHANGED,
    TEMPLATE_COMPLEX_VALUE,
    TEMPLATE_DELETED,
)


def flatten_diff(diff: list[dict], parent: str = "") -> list[str]:
    """
    Recursively flattens the diff structure into plain format with full paths.

    Args:
        diff (list[dict]): The structured diff data.
        parent (str, optional): The parent path for nested values.
                                Defaults to an empty string.

    Returns:
        list[str]: A list of formatted strings representing the diff.
    """
    flat_diff = []
    formatter_functions = formatters_plain(parent)

    for node in diff:
        type_ = node["type"]
        formatted_text = formatter_functions[type_](node)

        if isinstance(formatted_text, list):
            flat_diff.extend(formatted_text)
        elif formatted_text:
            flat_diff.append(formatted_text)

    return flat_diff


def formatters_plain(parent: str = "") -> dict:
    """
    Returns a dictionary of formatter functions for each diff type in plain
    format.

    Args:
        parent (str): The parent path for nested values.

    Returns:
        dict: Dictionary of formatter functions for each diff type.
    """

    templates = {
        "added": lambda node: TEMPLATE_ADDED.format(
            path=f"{parent}.{node['key']}" if parent else node["key"],
            new_value=format_value_plain(node["new_value"]),
        ),
        "removed": lambda node: TEMPLATE_DELETED.format(
            path=f"{parent}.{node['key']}" if parent else node["key"]
        ),
        "changed": lambda node: TEMPLATE_CHANGED.format(
            path=f"{parent}.{node['key']}" if parent else node["key"],
            old_value=format_value_plain(node["old_value"]),
            new_value=format_value_plain(node["new_value"]),
        ),
        "nested": lambda node: flatten_diff(
            node["children"],
            f"{parent}.{node['key']}" if parent else node["key"],
        ),
        "unchanged": lambda node: "",
    }

    return templates


def format_value_plain(value: object) -> str:
    """
    Formats a value for plain format output.

    Args:
        value: The value to format.

    Returns:
        str: A string representation of the value.
    """
    if isinstance(value, dict):
        return TEMPLATE_COMPLEX_VALUE
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, (int, float)):
        return str(value)
    return f"'{value}'"


def format_diff_plain(diff: list[dict]) -> str:
    """
    Formats the diff into plain text format.

    Args:
        diff (list[dict]): The structured diff data.

    Returns:
        str: A formatted plain-text representation of the diff.
    """
    flat_diff = flatten_diff(diff)
    return "\n".join(flat_diff)
