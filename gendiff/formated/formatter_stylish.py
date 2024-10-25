ADD = "+ "
DELETE = "- "
REPLACER = " "
INDENT_SIZE = 4


def format_added(key, value, indent):
    return f"{indent}+ {key}: {value}"


def format_removed(key, value, indent):
    return f"{indent}- {key}: {value}"


def format_changed(key, old_value, new_value, indent):
    return [
        f"{indent}- {key}: {old_value}",
        f"{indent}+ {key}: {new_value}",
    ]


def format_unchanged(key, value, indent):
    return f"{indent}  {key}: {value}"


def format_nested(key, children, indent, depth):
    nested_diff = format_diff_stylish(children, depth + 1)
    return f"{indent}  {key}: {nested_diff}"


def format_dict(value, depth):
    lines = []
    indent_size = 4
    current_indent = " " * (depth * indent_size)
    child_indent = " " * ((depth + 1) * indent_size)

    for key, val in value.items():
        formatted_val = format_value(val, depth + 1)
        lines.append(f"{child_indent}{key}: {formatted_val}")

    closing_bracket_indent = current_indent
    return "{\n" + "\n".join(lines) + f"\n{closing_bracket_indent}}}"  # noqa


def get_indent(depth):
    return " " * (depth * INDENT_SIZE)


def get_closing_bracket_indent(depth):
    return " " * ((depth - 1) * INDENT_SIZE)


def format_diff_stylish(diff, depth=1):
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
                        format_value(node["new_value"], depth),
                        current_indent,
                    )
                )
            case "removed":
                result.append(
                    format_removed(
                        key,
                        format_value(node["old_value"], depth),
                        current_indent,
                    )
                )
            case "changed":
                old_value, new_value = format_value(
                    node["old_value"], depth
                ), format_value(node["new_value"], depth)
                result.extend(
                    format_changed(key, old_value, new_value, current_indent)
                )
            case "unchanged":
                result.append(
                    format_unchanged(
                        key, format_value(node["value"], depth), current_indent
                    )
                )
            case "nested":
                result.append(
                    format_nested(key, node["children"], current_indent, depth)
                )

    result.append(f"{' ' * ((depth - 1) * INDENT_SIZE)}}}")
    return "\n".join(result)


def format_value(value, depth):
    match value:
        case bool():
            return str(value).lower()
        case None:
            return "null"
        case dict():
            return format_dict(value, depth)
        case _:
            return str(value)
