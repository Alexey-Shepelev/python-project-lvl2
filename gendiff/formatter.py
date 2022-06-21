from gendiff.formatters import to_stylish
from gendiff.formatters import to_plain
from gendiff.formatters import to_json


def get_formatted(data, format_):
    if format_ == 'stylish':
        return to_stylish(data)
    elif format_ == 'plain':
        return to_plain(data)
    elif format_ == 'json':
        return to_json(data)
    raise Exception('Unknown format!')
