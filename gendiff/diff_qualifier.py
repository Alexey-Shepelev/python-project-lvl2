from gendiff.file_parser import parse
from gendiff.diff_builder import get_diff
from gendiff.formatter import get_formatted
import os.path


def get_data(file):
    _, ext = os.path.splitext(file)
    data_format = ext.lstrip('.')
    with open(file) as data:
        output = parse(data, data_format)
    return output


def generate_diff(file_1, file_2, format_name='stylish'):
    content_1 = get_data(file_1)
    content_2 = get_data(file_2)
    diff = get_diff(content_1, content_2)
    return get_formatted(diff, format_name)
