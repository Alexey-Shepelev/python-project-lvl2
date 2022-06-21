from gendiff import gen_diff
import os.path
import pytest


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath('file'))
    return os.path.join(current_dir, 'tests', 'fixtures', file_name)


cases = [
    ('file1.json', 'file2.json', 'flat_stylish_answer', 'stylish'),
    ('file1.yml', 'file2.yml', 'flat_stylish_answer', 'stylish'),
    ('nested_file1.json', 'nested_file2.json', 'nested_stylish_answer', 'stylish'),
    ('nested_file1.yml', 'nested_file2.yml', 'nested_stylish_answer', 'stylish'),
    ('file1.json', 'file2.json', 'plain_answer', 'plain'),
    ('file1.yml', 'file2.yml', 'plain_answer', 'plain'),
    ('nested_file1.json', 'nested_file2.json', 'nested_plain_answer', 'plain'),
    ('nested_file1.yml', 'nested_file2.yml', 'nested_plain_answer', 'plain'),
    ('file1.json', 'file2.json', 'json_answer', 'json'),
    ('file1.yml', 'file2.yml', 'json_answer', 'json'),
    ('nested_file1.json', 'nested_file2.json', 'nested_json_answer', 'json'),
    ('nested_file1.yml', 'nested_file2.yml', 'nested_json_answer', 'json')
]


@pytest.mark.parametrize('file1,file2,answer,format_name', cases)
def test_gen_diff(file1, file2, answer, format_name):
    with open(get_fixture_path(answer), 'r') as answer:
        f1 = get_fixture_path(file1)
        f2 = get_fixture_path(file2)
        assert gen_diff(f1, f2, format_name) == answer.read()


def test_exeption():
    with pytest.raises(Exception) as e:
        gen_diff(get_fixture_path('file1.yml'), get_fixture_path('stylish'))
    assert str(e.value) == 'Wrong file format!'
