#!/usr/bin/python3
"""This Module contains a function read_file  that reads
and print file conrents.
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
