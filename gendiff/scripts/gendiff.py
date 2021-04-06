"""Function to do something interesting.

This module can do magic shit
Output of the function
"""
import argparse
import json


def generate_diff(file1_path: str, file2_path: str) -> str:
    """**summary line** Function generate diff for flat json.

    Args:
        file1_path: path to json file1
        file2_path: path to json file2

    # noqa: DAR201
    """
    file1 = json.load(open(file1_path))  # noqa: WPS515
    file2 = json.load(open(file2_path))  # noqa: WPS515
    diff = []
    for key in sorted(file1):
        key = str(key)
        if key in file2:
            if file1.get(key) == file2.get(key):
                diff.append('    {0}: {1}'.format(key, str(file1[key])))
            else:
                diff.append('  - {0}: {1}'.format(key, str(file1[key])))
                diff.append('  + {0}: {1}'.format(key, str(file2.get(key))))
        else:
            diff.append('  - {0}: {1}'.format(key, str(file1[key])))
    for key2 in sorted(file2):
        if key2 not in file1:
            diff.append('  + {0}: {1}'.format(key2, str(file2[key2])))
#    print('{{\n{0}\n}}'.format('\n'.join(diff)))
    return '{{\n{0}\n}}'.format('\n'.join(diff))


def main():
    """Do main stuff."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    file1_path = args.first_file
    file2_path = args.second_file
    return generate_diff(file1_path, file2_path)


if __name__ == '__main__':
    main()
