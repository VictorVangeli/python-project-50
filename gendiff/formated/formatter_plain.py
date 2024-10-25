def format_diff_plain(diff):
    to_diff = []

    for info in diff:
        key = info["key"]
        type_ = info["type"]

        match type_:
            case "added":
                to_diff.append(f"+ {key}: {info['new_value']}")
            case "removed":
                to_diff.append(f"- {key}: {info['old_value']}")
            case "changed":
                to_diff.append(f"- {key}: {info['old_value']}")
                to_diff.append(f"+ {key}: {info['new_value']}")
            case "unchanged":
                to_diff.append(f"  {key}: {info['value']}")

    return "\n".join(to_diff)
