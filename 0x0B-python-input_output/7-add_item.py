#!/usr/bin/python3
"""Script that adds all arguments to a Python list, and
then save them to a file:
"""


import sys
import os.path


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    json_list = load_file(filename)
except Exception:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_file(json_list, filename)
