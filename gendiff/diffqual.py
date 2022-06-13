import json
from gendiff.file_parser import parser


def gen_diff(file_1, file_2):
    content_1 = parser(file_1)
    content_2 = parser(file_2)
    diff = dict()
    for key in sorted(content_1.keys() | content_2.keys()):
        if key not in content_1 and key in content_2:
            diff['+ ' + key] = content_2[key]
        elif key in content_1 and key not in content_2:
            diff['- ' + key] = content_1[key]
        elif content_1[key] == content_2[key]:
            diff['  ' + key] = content_1[key]
        else:
            diff['- ' + key] = content_1[key]
            diff['+ ' + key] = content_2[key]

    return json.dumps(
        diff, separators=('', ': '), indent=2
    ).replace('"', '')
