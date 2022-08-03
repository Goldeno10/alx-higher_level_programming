#!/usr/bin/python3
"""This module contains pascal_triangle() function.
"""


def pascal_triangle(n):
    """ Function that returns the pascal triangle
    Args:
        n: number of lines
    Returns:
        A list of lists of integers
        representing the Pascal’s triangle of n:
    """

    pascal_list = []
    prev = []

    for i in range(n):
        res_list = []
        p1 = -1
        p2 = 0
        for j in range(len(prev) + 1):
            if p1 == -1 or p2 == len(prev):
                res_list += [1]
            else:
                res_list += [prev[p1] + prev[p2]]
            p1 += 1
            p2 += 1
        pascal_list.append(res_list)
        prev = res_list[:]

    return (pascal_list)
