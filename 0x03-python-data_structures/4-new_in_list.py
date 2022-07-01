#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_1 = len(my_list) - 1
    list_cpy = [item for item in my_list]
    if idx < 0 or idx > len_1:
        return (my_list)
    list_cpy[idx] = element
    return (list_cpy)
