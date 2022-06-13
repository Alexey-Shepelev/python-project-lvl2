import json
import yaml


def parser(file):
    if file.endswith('.json'):
        return json.load(open(file))
    elif file.endswith('.yml') or file.endswith('.yaml'):
        return yaml.safe_load(open(file))
    raise Exception('Wrong file format!')
