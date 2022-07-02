#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_1 = len(my_list) - 1
    while len_1 >= 0:
        print("{:d}".format(my_list[len_1]))
        len_1 -= 1
