import json


def sorted_dictionary(d):
    new_d = d.copy()
    new_d = dict(sorted(new_d.items(), key=lambda x: x[0][0]))
    for v in new_d.values():
        if v is True:
            v = 'true'
        if v is False:
            v = 'false'
    return new_d


def make_string(d1, d2):
    s = ''
    for k, v in d1.items():
        if k not in d2:
            s = s + (f' - {k}: {v}\n')
        elif d1[k] == d2[k]:
            s = s + (f'   {k}: {v}\n')
        else:
            s = s + (f' - {k}: {v}\n')
            s = s + (f' + {k}: {d2[k]}\n')
    for k, v in d2.items():
        if k not in d1:
            s = s + (f' + {k}: {v}\n')
    result = '{\n' + s + '}'
    return result


def diff_key(d1, d2):
    new_d1 = sorted_dictionary(d1)
    new_d2 = sorted_dictionary(d2)
    return make_string(new_d1, new_d2)


def generate_diff(file1_path, file2_path):
    f1_open = open(file1_path)
    f2_open = open(file2_path)
    f1 = json.load(f1_open)
    f2 = json.load(f2_open)
    result = diff_key(f1, f2)
    return result
