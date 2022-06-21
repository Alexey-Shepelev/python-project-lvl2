import json


def convert(value):
    """
    Convert value from Python to plain format
    """
    if value is None or isinstance(value, bool):
        return json.dumps(value)
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, dict):
        return '[complex value]'
    return value


def get_plain(data, parent=[]):
    result = []
    for key, sub_dict in data.items():
        type_ = sub_dict.get('type')
        value = sub_dict.get('value')
        path = parent + [key]
        if type_ == 'nested':
            result.append(get_plain(value, path))
        elif type_ == 'added':
            result.append(f'Property \'{".".join(path)}\' '
                          f'was added with value: {convert(value)}')
        elif type_ == 'removed':
            result.append(f'Property \'{".".join(path)}\' was removed')
        elif type_ == 'changed':
            result.append(
                f'Property \'{".".join(path)}\' was updated. '
                f'From {convert(value.get("old_value"))} '
                f'to {convert(value.get("new_value"))}')
    return '\n'.join(result)