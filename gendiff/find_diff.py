def find_diff(text_first_file, text_second_file):
    to_diff = []

    all_keys = sorted(
        set(text_first_file.keys()).union(set(text_second_file.keys()))
    )

    for key in all_keys:
        if key not in text_second_file:
            to_diff.append(f"{key}: {text_first_file[key]}")
        elif key not in text_first_file:
            to_diff.append(f"{key}: {text_second_file[key]}")
        elif text_first_file[key] != text_second_file[key]:
            to_diff.append(f"{key}: {text_first_file[key]}")
            to_diff.append(f"{key}: {text_second_file[key]}")
        else:
            to_diff.append(f"{key}: {text_first_file[key]}")

    result = "\n".join(to_diff)
    return result
