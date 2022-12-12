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


def stylish(value, replacer=' ', space_count=2):
    plus = space_count

    def walk(value, replacer, space_count):
        value = sorted_dict(value)
        line = ''
        end = space_count - plus
        for k, v in value.items():
            if (not
               (k.startswith('+') or k.startswith('-') or k.startswith('  '))):
                k = '  ' + k
            if isinstance(v, dict):
                v = walk(v, replacer, space_count + plus * 2)
            line = line + (f'{replacer*space_count}{k}: {v}\n')
        return ('{\n' + line + replacer * end + '}')
    return walk(value, replacer, space_count)
