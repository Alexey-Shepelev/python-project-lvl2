import json


def generate_diff(file_1, file_2):
    content_1 = json.load(open(file_1))
    content_2 = json.load(open(file_2))
    result = dict()
    for key in content_1.keys() & content_2.keys():
        if content_1[key] == content_2[key]:
            result['  ' + key] = content_1[key]
        else:
            result['- ' + key] = content_1[key]
            result['+ ' + key] = content_2[key]
    for key in content_1.keys() - content_2.keys():
        result['- ' + key] = content_1[key]
    for key in content_2.keys() - content_1.keys():
        result['+ ' + key] = content_2[key]
    sorted_result = dict(sorted(result.items(), key=lambda item: item[0][2:]))
    return json.dumps(
        sorted_result, separators=('', ': '), indent=2).replace('"', '')
