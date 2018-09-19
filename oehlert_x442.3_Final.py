#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    "-d", "--directory", help="Specify directory to read", dest="directory"
)
args, remaining_argv = parser.parse_known_args()

d = args.directory


def find_files(directory):
    """ Builds list of files inside directory"""
    all_files = os.listdir(directory)
    extensions = {}

    for i in all_files:
        _, ext = os.path.splitext(i)
        if ext == "":
            ext = "empty"
        if ext in extensions:
            extensions[ext] += 1
        else:
            extensions[ext] = 1

    return extensions


def build_extension_dicts(extensions):
    """ Build individual lists for each file extension type """
    for key in extensions:
        pass


def get_file_info(d, extensions):
    """ Takes list of files in dir with given extension and
    calculates min, average, and max size of those files """
    for key in extensions:
        for f in os.listdir(d):
            if f.endswith(key):
                pass


if __name__ == "__main__":
    extensions = find_files(d)
    get_file_info(d, extensions)
