#!/usr/bin/python3
"""Contains a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers. """
    li = list_of_integers
    i = 0
    list_len = len(list_of_integers)
    j = list_len - 1
    p_E = 0
    p_B = 0
    peak = 0
    if list_len < 1:
        return None
    if list_len == 1:
        return li[0]
    if list_of_integers and list_len > 1:
        while i <= j:
            p_B = li[i] if li[i] > p_B else p_B
            p_E = li[j] if li[j] > p_E else p_E
            i += 1
            j -= 1
        peak = p_B if p_B > p_E else p_E
    return peak
