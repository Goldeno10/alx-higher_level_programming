#!/usr/bin/python3
def max_integer(my_list=[]):
    _len = len(my_list)
    if _len < 1:
        return(None)
    a = my_list[0]
    for i in range(1, _len):
        if a < my_list[i]:
            a = my_list[i]
    return(a)
