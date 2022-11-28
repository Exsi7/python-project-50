from gendiff import generate_diff


file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'

def test_generate_diff():
    f = open('tests/fixtures/result_json.txt', 'r')
    assert generate_diff(file1, file2) == f.read()