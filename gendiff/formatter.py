from gendiff.formatters import get_stylish
from gendiff.formatters import get_plain
from gendiff.formatters import get_json


def get_formatted(data, format_):
    if format_ == 'stylish':
        return get_stylish(data)
    elif format_ == 'plain':
        return get_plain(data)
    elif format_ == 'json':
        return get_json(data)
    raise Exception('Unknown format!')
