#!/usr/bin/python3

from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    file1, file2, output_format = parse_args()
    diff = generate_diff(file1, file2, output_format)
    print(diff)


if __name__ == '__main__':
    main()
