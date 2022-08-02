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

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
