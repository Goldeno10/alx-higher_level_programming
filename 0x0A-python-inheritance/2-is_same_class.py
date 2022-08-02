#!/usr/bin/python3
"""This module contains is_same_class function
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an
    instance of the specified clas
    otherwise False """
    return (type(obj) == a_class)
