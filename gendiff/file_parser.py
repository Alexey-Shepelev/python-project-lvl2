import json
import yaml


def parse(file, file_format):
    if file_format == 'json':
        return json.load(open(file))
    elif file_format in ('yml', 'yaml'):
        return yaml.safe_load(open(file))
    raise Exception('Wrong file format!')
