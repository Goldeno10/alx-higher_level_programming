#!/usr/bin/python3
"""This module contains a function that adds a new 
attribute to an object if it’s possible:
"""


def add_attribute(obj, name, value):
    """ Function that adds a new attribute to an object
    Args:
        obj: object
        name: attribute name
        value: attribute value
    Raises:
        TypeError: when the attribute can't be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
