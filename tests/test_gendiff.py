from gendiff import generate_diff


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