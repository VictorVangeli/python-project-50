from typing import Any, Dict, List, Tuple


def removed_diff(key: str, old_value: Any) -> Dict[str, Any]:
    """
    Creates a dictionary representing the removal of a key.

    Args:
        key (str): The key that was removed.
        old_value (Any): The previous value associated with the key.

    Returns:
        Dict[str, Any]: A dictionary representing a removed key and its old
        value.
    """
    return {
        "key": key,
        "type": "removed",
        "old_value": old_value,
    }


def added_diff(key: str, new_value: Any) -> Dict[str, Any]:
    """
    Creates a dictionary representing the addition of a key.

    Args:
        key (str): The key that was added.
        new_value (Any): The new value associated with the key.

    Returns:
        Dict[str, Any]: A dictionary representing an added key and its new
        value.
    """
    return {
        "key": key,
        "type": "added",
        "new_value": new_value,
    }


def changed_diff(key: str, old_value: Any, new_value: Any) -> Dict[str, Any]:
    """
    Creates a dictionary representing the modification of a key's value.

    Args:
        key (str): The key whose value has changed.
        old_value (Any): The old value of the key.
        new_value (Any): The new value of the key.

    Returns:
        Dict[str, Any]: A dictionary representing a changed key, with its old
        and new values.
    """
    return {
        "key": key,
        "type": "changed",
        "old_value": old_value,
        "new_value": new_value,
    }


def unchanged_diff(key: str, value: Any) -> Dict[str, Any]:
    """
    Creates a dictionary representing an unchanged key.

    Args:
        key (str): The key that has not changed.
        value (Any): The current value of the key.

    Returns:
        Dict[str, Any]: A dictionary representing an unchanged key and its
        value.
    """
    return {
        "key": key,
        "type": "unchanged",
        "value": value,
    }


def nested_diff(
    key: str, value_1: Dict[str, Any], value_2: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Creates a dictionary representing the difference between two nested
    dictionaries.

    Args:
        key (str): The key representing the nested dictionaries.
        value_1 (Dict[str, Any]): The first dictionary (old state).
        value_2 (Dict[str, Any]): The second dictionary (new state).

    Returns:
        Dict[str, Any]: A dictionary representing the difference in nested
        dictionaries.
    """
    return {
        "key": key,
        "type": "nested",
        "children": find_diff(value_1, value_2),
    }


def process_key(
    diff_tuple: Tuple[str, Any, Any, Dict[str, Any], Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Processes a key and its values to determine the type of change (added,
    removed, changed, unchanged, nested).

    Args:
        diff_tuple (Tuple[str, Any, Any, Dict[str, Any], Dict[str, Any]]): A
        tuple containing the key, old value, new value, and the two
        dictionaries being compared.

    Returns:
        Dict[str, Any]: A dictionary representing the type of change for the
        key.
    """
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


def process_diff(
    all_keys: List[str],
    text_first_file: Dict[str, Any],
    text_second_file: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """
    Processes all keys in the dictionaries and determines the differences
    between the two dictionaries.

    Args:
        all_keys (List[str]): A list of all unique keys from both dictionaries.
        text_first_file (Dict[str, Any]): The first dictionary.
        text_second_file (Dict[str, Any]): The second dictionary.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing the
        differences for each key.
    """
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


def find_diff(
    text_first_file: Dict[str, Any], text_second_file: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Finds the differences between two dictionaries and returns a list of
    changes.

    Args:
        text_first_file (Dict[str, Any]): The first dictionary to compare.
        text_second_file (Dict[str, Any]): The second dictionary to compare.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing the
        differences between the two dictionaries.
    """
    all_keys = sorted(text_first_file.keys() | text_second_file.keys())
    return process_diff(all_keys, text_first_file, text_second_file)
