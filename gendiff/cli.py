import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.' 
    )
    parser.add_argument('first file')
    parser.add_argument('second file')
    return parser.parse_args()
