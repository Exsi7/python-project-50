from gendiff.format.stylish import sorted_dict


def create_path(path, k):
    if path == '':
        return path + k
    else:
        return path + '.' + k


def format_values(v):
    list_format = ['true', 'false', 'null', '[complex value]']
    if v not in list_format and not isinstance(v, int):
        v = (f'\'{v}\'')
    return v


def create_line(k, v, value, line, begin):
    v = format_values(v)
    if '+ ' + k[2:] in value and '- ' + k[2:] in value:
        if k == '- ' + k[2:]:
            line = line + (f'{begin} was updated. From {v} to ')
        else:
            line = line + (f'{v}\n')
    elif k.startswith('+ '):
        line = line + (f'{begin} was added with value: {v}\n')
    elif k.startswith('- '):
        line = line + (f'{begin} was removed\n')
    return line


def plain(value):
    def walk(value, path):
        value = sorted_dict(value)
        line = ''
        for k, v in value.items():
            pathd = create_path(path, k[2:])
            begin = (f'Property \'{pathd}\'')
            if k.startswith('  ') and isinstance(v, dict):
                line = line + walk(v, pathd)
            elif isinstance(v, dict):
                v = '[complex value]'
            line = create_line(k, v, value, line, begin)
        return line
    return walk(value, '')
