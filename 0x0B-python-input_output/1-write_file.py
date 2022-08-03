#!/usr/bin/python3
"""This Module contains a function write_file that writes
to a file.
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    num_of_chars = 0
    with open(filename, 'w', encoding='utf-8') as f:
        num_of_chars = f.write(str(text))
    return (num_of_chars)
