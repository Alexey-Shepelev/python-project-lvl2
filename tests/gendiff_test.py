from gendiff import generate_diff

FLAT_JSON_1 = 'tests/fixtures/file1.json'
FLAT_JSON_2 = 'tests/fixtures/file2.json'
FLAT_JSON_ANSWER = 'tests/fixtures/flat_json_answer'


def get_file_content(file):
    with open(file) as file:
        content = file.read()
    return content


def test_generate_diff():
    assert generate_diff(FLAT_JSON_1, FLAT_JSON_2) == get_file_content(FLAT_JSON_ANSWER)
