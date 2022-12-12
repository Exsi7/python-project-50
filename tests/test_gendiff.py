from gendiff import generate_diff
from gendiff.format.plain import plain
from gendiff.format.format_json import format_json
from gendiff.format.stylish import stylish


file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'
file3 = 'tests/fixtures/file3.yml'
file4 = 'tests/fixtures/file4.yml'

def test_generate_diff_json():
    f = open('tests/fixtures/result_json.txt', 'r')
    diff = generate_diff(file1, file2)
    assert stylish(diff) == f.read()


def test_generate_diff_yaml():
    f = open('tests/fixtures/result_yaml.txt', 'r')
    diff = generate_diff(file3, file4)
    assert stylish(diff) == f.read()


def test_plain():
    f = open('tests/fixtures/result_plain.txt', 'r')
    result = f.read()
    diff1 = generate_diff(file1, file2)
    diff2 = generate_diff(file3, file4)
    assert plain(diff1) == result
    assert plain(diff2) == result


def test_format_json():
    f = open('tests/fixtures/result_f_json.txt', 'r')
    result = f.read()
    diff1 = generate_diff(file1, file2)
    diff2 = generate_diff(file3, file4)
    assert format_json(diff1) == result
    assert format_json(diff2) == result
