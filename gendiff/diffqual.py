from gendiff.file_parser import parser
from gendiff.diff_builder import get_diff
from gendiff.formaters import get_formatted


def gen_diff(file_1, file_2, format_='stylish'):
    content_1 = parser(file_1)
    content_2 = parser(file_2)
    diff = get_diff(content_1, content_2)
    return get_formatted(diff, format_)
