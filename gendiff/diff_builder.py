def get_diff(data_1, data_2):
    union_dict = dict()
    for key in sorted(data_1.keys() | data_2.keys()):
        if key not in data_1:
            union_dict[key] = {
                'type': 'added',
                'value': data_2[key]
            }
        elif key not in data_2:
            union_dict[key] = {
                'type': 'removed',
                'value': data_1[key]
            }
        elif data_1[key] == data_2[key]:
            union_dict[key] = {
                'type': 'unchanged',
                'value': data_1[key]
            }
        elif isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
            union_dict[key] = {
                'type': 'nested',
                'value': get_diff(data_1[key], data_2[key])
            }
        else:   # data_1[key] != data_2[key]
            union_dict[key] = {
                'type': 'changed',
                'value': {
                    'old_value': data_1[key],
                    'new_value': data_2[key]
                }
            }
    return union_dict
