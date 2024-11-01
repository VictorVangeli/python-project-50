from gendiff.const import INDENT_SIZE


def format_added(key: str, value: str, indent: str) -> str:
    """
    Formats a string for an added element.

    Args:
        key (str): The element's key.
        value (str): The element's value.
        indent (str): Current indentation level.

    Returns:
        str: Formatted string representing the added element.
    """
    return f"{indent}+ {key}: {value}"


def format_removed(key: str, value: str, indent: str) -> str:
    """
    Formats a string for a removed element.

    Args:
        key (str): The element's key.
        value (str): The element's value.
        indent (str): Current indentation level.

    Returns:
        str: Formatted string representing the removed element.
    """
    return f"{indent}- {key}: {value}"


def format_changed(
    key: str, old_value: str, new_value: str, indent: str
) -> list:
    """
    Formats strings for a changed element.

    Args:
        key (str): The element's key.
        old_value (str): The element's old value.
        new_value (str): The element's new value.
        indent (str): Current indentation level.

    Returns:
        list: List of formatted strings for the changed element.
    """
    return [
        f"{indent}- {key}: {old_value}",
        f"{indent}+ {key}: {new_value}",
    ]


def format_unchanged(key: str, value: str, indent: str) -> str:
    """
    Formats a string for an unchanged element.

    Args:
        key (str): The element's key.
        value (str): The element's value.
        indent (str): Current indentation level.

    Returns:
        str: Formatted string representing the unchanged element.
    """
    return f"{indent}  {key}: {value}"


def get_indent(depth: int) -> str:
    """
    Returns the current indentation based on the nesting depth.

    Args:
        depth (int): Current nesting depth.

    Returns:
        str: Indentation string.
    """
    return " " * (depth * INDENT_SIZE)


def get_closing_bracket_indent(depth: int) -> str:
    """
    Returns the indentation for the closing bracket based on nesting depth.

    Args:
        depth (int): Current nesting depth.

    Returns:
        str: Indentation string for the closing bracket.
    """
    return " " * ((depth - 1) * INDENT_SIZE)
