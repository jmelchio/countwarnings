#!/usr/bin/env python3

import os
import subprocess
import sys


def process_directory(directory=None):
    if directory is None:
        return 1

    cur_dir = os.path.curdir
    os.chdir(directory)
    process_results = subprocess.run(['git', 'diff', '--name-only'], stdout=subprocess.PIPE)
    diff_list = str(process_results.stdout, sys.stdout.encoding).split()
    print(diff_list)

    dir_list = set()
    for file in diff_list:
        dir_list.add(os.path.dirname(os.path.abspath(file)))

    print(dir_list)
    os.chdir(cur_dir)
    return 0


def count_warnings(*args):
    directory = None
    if (len(args)) == 0:
        if (len(sys.argv)) < 2:
            print('Usage %s DIRECTORY' % sys.argv[0])
            exit(1)
        else:
            directory = sys.argv[1]
    else:
        directory = args[0]

    if not os.path.exists(directory):
        print('Usage %s DIRECTORY' % directory)
        exit(1)

    print('Directory passed in: %s' % directory)

    return process_directory(directory)


if __name__ == '__main__':
    exit(count_warnings())
