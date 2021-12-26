#!/usr/bin/python3
""" This script  """
from sys import argv, exit
from os.path import exists


if __name__ == "__main__":
    if len(argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html')
        exit(1)
    if not exists(argv[1]):
        print("Missing {}".format(argv[1]))
