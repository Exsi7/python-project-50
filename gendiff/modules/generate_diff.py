import json
import yaml


def open_file(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    else:
        return yaml.safe_load(open(file_path))


def sort_k(k):
    if k[0].startswith('+') or k[0].startswith('-') or k[0].startswith('  '):
        return k[0][2:]
    else:
        return k[0]


def sorted_dict(d, n=0):
    new_d = d.copy()
    new_d = dict(sorted(new_d.items(), key=lambda x: sort_k(x)))
    for k, v in new_d.items():
        if v is True:
            new_d[k] = 'true'
        if v is False:
            new_d[k] = 'false'
        if v is None:
            new_d[k] = 'null'
    return new_d


def diff_dict(d1, d2):
    result = {}
    keys = list(d1.keys() | d2.keys())
    for k in keys:
        if k not in d1:
            result['+ ' + str(k)] = d2[k]
        elif k not in d2:
            result['- ' + str(k)] = d1[k]
        elif isinstance(d1[k], dict) and isinstance(d2[k], dict):
            result['  ' + str(k)] = diff_dict(d1[k], d2[k])
        elif d1[k] == d2[k]:
            result['  ' + str(k)] = d1[k]
        else:
            result['- ' + str(k)] = d1[k]
            result['+ ' + str(k)] = d2[k]
    return result


def generate_diff(file1_path, file2_path):
    f1 = open_file(file1_path)
    f2 = open_file(file2_path)
    diff = diff_dict(f1, f2)
    return diff
