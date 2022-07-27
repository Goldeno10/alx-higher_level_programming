#!/usr/bin/python3
"""This Module contains a function matrix_divided.
It decides a given matrix by a given devisor
Note matrix must be a list of list of integers/floats

"""


def matrix_divided(matrix, div):
    """matrix_devided: Devides the items of a list of
    list of ints/floats by a devissor div.

    Args:
        matrix (list): list of lists of ints/floats
        div (int/float): The devissor

    Returns:
        A new matrix

    """

    if type(matrix) != list:
        raise TypeError("""matrix must be a matrix (list o
                lists) of integers/floats""")
    for it in matrix:
        if type(it) != list:
            raise TypeError("""matrix must be a matrix
                    list of lists) of integers/floats""")
        for i in it:
            if type(i) not in [int, float]:
                raise TypeError("""matrix must be a matrix(
                        iist of lists) of
                        integers/floats""")
    list_len = len(matrix[0])
    for item in matrix:
        if len(item) != list_len:
            raise TypeError("""Each row of the matrix must
                    have the same size""")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round((i/div), 2) for i in it] for it in matrix]
    return(new_matrix)
