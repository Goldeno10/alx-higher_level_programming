#!/usr/bin/python3
"""Contains an empty class BaseGeometry
"""


class BaseGeometry:
    """A class with and unimplemented function"""

    def area(self):
        """A Public instance method: def area
        that raises an Exception with the message
        'area() is not implemented'
        """

        raise NameError("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method:integer_validator
        that validates 'value' parameter"""

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
