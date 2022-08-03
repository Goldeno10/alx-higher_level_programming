#!/usr/bin/python3
"""This module contains load_from_json_file() function
"""


import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'
    """
    with open(filename, 'r', encoding='utf-8') as f:
        new_f = json.load(f)
    return(new_f)
