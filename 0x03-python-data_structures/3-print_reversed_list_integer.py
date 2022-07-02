#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_1 = len(my_list) - 1
    if not my_list:
        pass
    else:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
