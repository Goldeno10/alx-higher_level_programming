#!/usr/bin/python3
def no_c(my_string):
    str_list = [i for i in my_string if i not in "cC"]
    new_str = ("").join(str_list)
    return (new_str)
