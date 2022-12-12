from gendiff import generate_diff
from gendiff.format.plain import plain
from gendiff.format.format_json import format_json


file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'
file3 = 'tests/fixtures/file3.yml'
file4 = 'tests/fixtures/file4.yml'

def test_generate_diff_json():
    f = open('tests/fixtures/result_json.txt', 'r')
    assert generate_diff(file1, file2) == f.read()


def test_generate_diff_yaml():
    f = open('tests/fixtures/result_yaml.txt', 'r')
    assert generate_diff(file3, file4) == f.read()


def test_plain():
    f = open('tests/fixtures/result_plain.txt', 'r')
    result = f.read()
    assert generate_diff(file1, file2, 'plain') == result
    assert generate_diff(file3, file4, 'plain') == result


def test_format_json():
    f = open('tests/fixtures/result_f_json.txt', 'r')
    result = f.read()
    assert generate_diff(file1, file2, 'json') == result
    assert generate_diff(file1, file2, 'json') == result
