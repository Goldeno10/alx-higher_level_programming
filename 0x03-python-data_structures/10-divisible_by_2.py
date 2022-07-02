#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    _len = len(my_list) - 1
    if _len >= 0:
        new_list = [(True if i % 2 == 0 else False) for i in my_list]
    return(new_list)
