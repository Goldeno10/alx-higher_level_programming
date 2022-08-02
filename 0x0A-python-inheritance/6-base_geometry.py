#!/usr/bin/python3
"""Contains an empty class BaseGeometry
"""


class BaseGeometry:
    """A class with and unimplemented function"""

    def ___init___(self):
        """An Unimplenented initializer"""

        pass
    
    def area(self):
        """A Public instance method: def area(self): 
        that raises an Exception with the message 
        'area() is not implemented'
        """

        raise NameError("area() is not implemented")

