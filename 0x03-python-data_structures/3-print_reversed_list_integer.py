#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    _len = len(my_list)
    if not my_list or _len < 1:
        pass
    else:
        my_list.reverse()
        for i in range(_len):
            print("{:d}".format(my_list[i]))
