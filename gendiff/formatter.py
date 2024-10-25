ADD = "+ "
DELETE = "- "
REPLACER = " "
SPACESCOUNT = 4


def get_formatter(format_name):
    if format_name == "plain":
        return format_diff_plain
    elif format_name == "stylish":
        return format_diff_stylish


def format_diff_plain(diff):
    to_diff = []

    for info in diff:
        key = info["key"]
        type_ = info["type"]

        if type_ == "added":
            to_diff.append(f"+ {key}: {info['new_value']}")
        elif type_ == "removed":
            to_diff.append(f"- {key}: {info['old_value']}")
        elif type_ == "changed":
            to_diff.append(f"- {key}: {info['old_value']}")
            to_diff.append(f"+ {key}: {info['new_value']}")
        elif type_ == "unchanged":
            to_diff.append(f"  {key}: {info['value']}")

    return "\n".join(to_diff)

def format_diff_stylish(diff, depth=1):
    indent_size = 4
    current_indent = ' ' * (depth * indent_size - 2)
    deep_indent = ' ' * (depth * indent_size)
    result = ["{"]

    for node in diff:
        key = node["key"]
        type_ = node["type"]

        if type_ == "added":
            result.append(f"{current_indent}+ {key}: {format_value(node['new_value'], depth)}")
        elif type_ == "removed":
            result.append(f"{current_indent}- {key}: {format_value(node['old_value'], depth)}")
        elif type_ == "changed":
            result.append(f"{current_indent}- {key}: {format_value(node['old_value'], depth)}")
            result.append(f"{current_indent}+ {key}: {format_value(node['new_value'], depth)}")
        elif type_ == "unchanged":
            result.append(f"{current_indent}  {key}: {format_value(node['value'], depth)}")
        elif type_ == "nested":
            nested_diff = format_diff_stylish(node["children"], depth + 1)
            result.append(f"{current_indent}  {key}: {nested_diff}")

    result.append(f"{' ' * ((depth - 1) * indent_size)}}}")
    return '\n'.join(result)


def format_value(value, depth):
    indent_size = 4
    deep_indent = ' ' * (depth * indent_size)

    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        lines = []
        for key, val in value.items():
            formatted_val = format_value(val, depth + 1)
            lines.append(f"{deep_indent}    {key}: {formatted_val}")
        return f"{{\n" + "\n".join(lines) + f"\n{deep_indent}}}"

    return str(value)
