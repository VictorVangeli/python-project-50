ADD = "+ "
DELETE = "- "
REPLACER = " "
INDENT_SIZE = 4


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
    indent_size = 4
    current_indent = " " * (depth * indent_size)
    child_indent = " " * ((depth + 1) * indent_size)

    for key, val in value.items():
        formatted_val = format_value_stylish(val, depth + 1)
        lines.append(f"{child_indent}{key}: {formatted_val}")

    closing_bracket_indent = current_indent
    return "{\n" + "\n".join(lines) + f"\n{closing_bracket_indent}}}"  # noqa


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

    for node in diff:
        key = node["key"]
        type_ = node["type"]

        match type_:
            case "added":
                result.append(
                    format_added(
                        key,
                        format_value_stylish(node["new_value"], depth),
                        current_indent,
                    )
                )
            case "removed":
                result.append(
                    format_removed(
                        key,
                        format_value_stylish(node["old_value"], depth),
                        current_indent,
                    )
                )
            case "changed":
                old_value, new_value = format_value_stylish(
                    node["old_value"], depth
                ), format_value_stylish(node["new_value"], depth)
                result.extend(
                    format_changed(key, old_value, new_value, current_indent)
                )
            case "unchanged":
                result.append(
                    format_unchanged(
                        key,
                        format_value_stylish(node["value"], depth),
                        current_indent,
                    )
                )
            case "nested":
                result.append(
                    format_nested(key, node["children"], current_indent, depth)
                )

    result.append(f"{' ' * ((depth - 1) * INDENT_SIZE)}}}")
    return "\n".join(result)


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
        case int():  # Обрабатываем числа
            return str(value)
        case dict():
            return format_dict(value, depth)
        case _:
            return str(value)
