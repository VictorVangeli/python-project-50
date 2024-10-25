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


def process_key(diff_tuple):
    key, old_value, new_value, text_first_file, text_second_file = diff_tuple

    if key not in text_second_file:
        return removed_diff(key, old_value)

    if key not in text_first_file:
        return added_diff(key, new_value)

    if isinstance(old_value, dict) and isinstance(new_value, dict):
        return nested_diff(key, old_value, new_value)

    if old_value != new_value:
        return changed_diff(key, old_value, new_value)

    return unchanged_diff(key, old_value)


def process_diff(all_keys, text_first_file, text_second_file):
    diff_data = [
        (
            key,
            text_first_file.get(key),
            text_second_file.get(key),
            text_first_file,
            text_second_file,
        )
        for key in all_keys
    ]

    return list(map(process_key, diff_data))


def find_diff(text_first_file, text_second_file):
    all_keys = sorted(text_first_file.keys() | text_second_file.keys())
    return process_diff(all_keys, text_first_file, text_second_file)
