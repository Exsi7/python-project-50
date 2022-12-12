import argparse
from gendiff import generate_diff
from gendiff.format.stylish import stylish
from gendiff.format.plain import plain
from gendiff.format.format_json import format_json

def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', choices=['plain', 'json'], default=stylish,
                        help='set format of output')
    args = parser.parse_args()
    if args.format == 'plain':
        print((generate_diff(args.first_file, args.second_file, plain)))
    elif args.format == 'json':
        print(generate_diff(args.first_file, args.second_file, format_json))
    else:
        print(generate_diff(args.first_file, args.second_file))
