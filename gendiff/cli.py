import argparse
from gendiff import generate_diff
from gendiff.modules.generate_diff import stylish, text_s


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', choices=['text_s'], default=stylish,
                        help='set format of output')
    args = parser.parse_args()
    print(args.format)
    if args.format == 'text_s':
        print((generate_diff(args.first_file, args.second_file, text_s)))
    else:
        print(generate_diff(args.first_file, args.second_file, args.format))
