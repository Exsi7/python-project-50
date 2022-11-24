import json


def sorted_dictionary(d):
    new_d = d.copy()
    new_d = dict(sorted(new_d.items(), key=lambda x: x[0][0]))
    return new_d


def diff_key(d1, d2):
    new_d1 = sorted_dictionary(d1)
    new_d2 = sorted_dictionary(d2)
    s = ''
    for k, v in new_d1.items():
        if v is True:
            v = 'true'
        if v is False:
            v = 'false'
        if k not in new_d2:
            s = s + (f' - {k}: {v}\n')
        elif new_d1[k] == new_d2[k]:
            s = s + (f'   {k}: {v}\n')
        else:
            s = s + (f' - {k}: {v}\n')
            s = s + (f' + {k}: {new_d2[k]}\n')
    for k, v in new_d2.items():
        if v is True:
            v = 'true'
        if v is False:
            v = 'false'
        if k not in new_d1:
            s = s + (f' + {k}: {v}\n')
    result = '{\n' + s + '}'
    return result


def generate_diff(file1_path, file2_path):
    f1_open = open(file1_path)
    f2_open = open(file2_path)
    f1 = json.load(f1_open)
    f2 = json.load(f2_open)
    result = diff_key(f1, f2)
    return result
