import json

TAB = '    '
STATUS_TYPES = {
    'added': '  + ',
    'removed': '  - ',
    'unchanged': '    '
}


def to_str(value):
    """
    Convert value from Python to json/yaml format
    """
    if value is None or isinstance(value, bool):
        return json.dumps(value)
    return value


def stringify(data, depth):
    if isinstance(data, dict):
        result = ['{']
        for key, value in data.items():
            result.append(f'{TAB * depth}{key}: {stringify(value, depth + 1)}')
        result.append(f'{TAB * (depth - 1)}}}')
        return '\n'.join(result)
    return to_str(data)


def get_stylish(data, depth=1):
    result = ['{']
    for key, sub_dict in data.items():
        type_ = sub_dict.get('type')
        value = sub_dict.get('value')
        if type_ == 'nested':
            result.append(f'{TAB * depth}{key}: {get_stylish(value, depth+1)}')
        elif type_ == 'changed':
            result.append(f'{TAB * (depth - 1)}{STATUS_TYPES["removed"]}{key}: '
                          f'{stringify(value.get("old_value"), depth + 1)}')
            result.append(f'{TAB * (depth - 1)}{STATUS_TYPES["added"]}{key}: '
                          f'{stringify(value.get("new_value"), depth + 1)}')
        else:
            result.append(f'{TAB * (depth - 1)}{STATUS_TYPES[type_]}{key}: '
                          f'{stringify(value, depth + 1)}')
    result.append(f'{TAB * (depth - 1)}}}')
    return '\n'.join(result)


def to_stylish(data):
    return get_stylish(data)
