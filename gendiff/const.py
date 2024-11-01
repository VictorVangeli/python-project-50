"""From formatted_plain"""

TEMPLATE_ADDED = "Property '{path}' was added with value: {new_value}"
TEMPLATE_DELETED = "Property '{path}' was removed"
TEMPLATE_CHANGED = (
    "Property '{path}' was updated. From {old_value} to {new_value}"
)
TEMPLATE_COMPLEX_VALUE = "[complex value]"


"""From formatter_stylish"""

ADD = "+ "
DELETE = "- "
REPLACER = " "
INDENT_SIZE = 4

INDENT_DICT = {
    "indent_size_for_simple": "",
    "indent_size_for_stylish": 4,
}
