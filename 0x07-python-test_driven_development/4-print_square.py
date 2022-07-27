#!/usr/bin/python3
"""This Module contain a function that prints a sqaure of
#s.
example:
    >>> print_sqaure(2)
    ##
    ##

"""


def print_square(size):
    """print_square prints a square of #s 

    Arg:
        size (int): size of the sqaure

    Retirns:
        Nothing
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (type(size) == float) and (size < 0):
        raise TypeError("size must be an integer")
    if size == 0:
        print()
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
