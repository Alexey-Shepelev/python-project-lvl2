from gendiff import gen_diff
import pytest

FLAT_JSON_1 = 'tests/fixtures/file1.json'
FLAT_JSON_2 = 'tests/fixtures/file2.json'
FLAT_YAML_1 = 'tests/fixtures/file1.yml'
FLAT_YAML_2 = 'tests/fixtures/file2.yml'
NESTED_JSON_1 = 'tests/fixtures/nested_file1.json'
NESTED_JSON_2 = 'tests/fixtures/nested_file2.json'
NESTED_YML_1 = 'tests/fixtures/nested_file1.yml'
NESTED_YML_2 = 'tests/fixtures/nested_file2.yml'

FLAT_STYLISH_ANSWER = 'tests/fixtures/flat_stylish_answer'
NESTED_STYLISH_ANSWER = 'tests/fixtures/nested_stylish_answer'

cases = [
    (FLAT_JSON_1, FLAT_JSON_2, FLAT_STYLISH_ANSWER),
    (FLAT_YAML_1, FLAT_YAML_2, FLAT_STYLISH_ANSWER),
    (NESTED_JSON_1, NESTED_JSON_2, NESTED_STYLISH_ANSWER),
    (NESTED_YML_1, NESTED_YML_2, NESTED_STYLISH_ANSWER)
]

def get_file_content(file):
    with open(file) as file:
        content = file.read()
    return content


@pytest.mark.parametrize('file1,file2,answer', cases)
def test_gen_diff(file1, file2, answer):
    assert gen_diff(file1, file2) == get_file_content(answer)


def test_exeption():
    with pytest.raises(Exception) as e:
        gen_diff(FLAT_YAML_1, FLAT_STYLISH_ANSWER)
    assert str(e.value) == 'Wrong file format!'
