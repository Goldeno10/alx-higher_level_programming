#!/usr/bin/python3
"""Add Integer
This module contains a function addinteger that
adds two integers together

"""


def add_integer(a, b=98):
    """add_integer add two integers a and b bith casted to int
    Args:
        a(int): integer one
        b(int): integer two
    Returns:
        An intger; the addition of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if not a:
        raise TypeError("""add_integer() missing 1 require
                positional argument: 'a'""")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return ((a) + (b))
