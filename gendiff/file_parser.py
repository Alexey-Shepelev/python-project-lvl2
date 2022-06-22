import json
import yaml


def parse(data, data_format):
    if data_format == 'json':
        return json.load(data)
    elif data_format in ('yml', 'yaml'):
        return yaml.safe_load(data)
    raise Exception('Wrong file format!')
