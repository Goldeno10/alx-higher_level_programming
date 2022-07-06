#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_t = list(sorted(a_dictionary))
    for it in dic_t:
        print("{}: {}".format(it, a_dictionary[it]))
