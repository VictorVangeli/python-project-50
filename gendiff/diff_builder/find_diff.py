def removed_diff(key, old_value):
    return {
        "key": key,
        "type": "removed",
        "old_value": old_value,
    }


def added_diff(key, new_value):
    return {
        "key": key,
        "type": "added",
        "new_value": new_value,
    }


def changed_diff(key, old_value, new_value):
    return {
        "key": key,
        "type": "changed",
        "old_value": old_value,
        "new_value": new_value,
    }


def unchanged_diff(key, value):
    return {
        "key": key,
        "type": "unchanged",
        "value": value,
    }


def nested_diff(key, value_1, value_2):
    return {
        "key": key,
        "type": "nested",
        "children": find_diff(value_1, value_2),
    }


def find_diff(text_first_file, text_second_file):
    diff = []
    all_keys = sorted(text_first_file.keys() | text_second_file.keys())

    for key in all_keys:
        old_value = text_first_file.get(key)
        new_value = text_second_file.get(key)

        if key not in text_second_file:
            diff.append(removed_diff(key, old_value))
        elif key not in text_first_file:
            diff.append(added_diff(key, new_value))
        elif isinstance(old_value, dict) and isinstance(new_value, dict):
            diff.append(nested_diff(key, old_value, new_value))
        elif old_value != new_value:
            diff.append(changed_diff(key, old_value, new_value))
        else:
            diff.append(unchanged_diff(key, old_value))

    return diff
