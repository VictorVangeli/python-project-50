TEMPLATE_ADDED = "Property '{path}' was added with value: {new_value}"
TEMPLATE_DELETED = "Property '{path}' was removed"
TEMPLATE_CHANGED = (
    "Property '{path}' was updated. From {old_value} to {new_value}"
)
TEMPLATE_COMPLEX_VALUE = "[complex value]"


def format_value(value):
    """Форматируем значение для plain-формата."""
    if isinstance(value, dict):
        return TEMPLATE_COMPLEX_VALUE
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return f"'{value}'"


def flatten_diff(diff, parent=""):
    """Рекурсивно преобразуем diff в плоский формат с полными путями."""
    flat_diff = []

    for node in diff:
        key = node["key"]
        type_ = node["type"]
        full_path = (
            f"{parent}.{key}" if parent else key
        )  # Формируем полный путь

        match type_:
            case "added":
                flat_diff.append(
                    TEMPLATE_ADDED.format(
                        path=full_path,
                        new_value=format_value(node["new_value"]),
                    )
                )
            case "removed":
                flat_diff.append(TEMPLATE_DELETED.format(path=full_path))
            case "changed":
                old_value = format_value(node["old_value"])
                new_value = format_value(node["new_value"])
                flat_diff.append(
                    TEMPLATE_CHANGED.format(
                        path=full_path,
                        old_value=old_value,
                        new_value=new_value,
                    )
                )
            case "nested":
                # Если это вложенная структура, вызываем flatten_diff рекурсивно
                flat_diff.extend(flatten_diff(node["children"], full_path))

    return flat_diff


def format_diff_plain(diff):
    """Форматируем плоскую структуру diff."""
    flat_diff = flatten_diff(diff)
    return "\n".join(flat_diff)
