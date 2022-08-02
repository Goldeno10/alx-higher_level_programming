#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public instance methods area and
    an integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
