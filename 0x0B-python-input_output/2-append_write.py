#!/usr/bin/python3
"""This modul contain the function append_write
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    num_of_chars = 0
    with open(filename, 'a', encoding='utf-8') as f:
        num_of_chars = f.write(str(text))
    return (num_of_chars)
