#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) < 1:
        return 0
    weight = sum([it[0] * it[1] for it in my_list])
    num = sum([it[1] for it in my_list])
    return weight / num
