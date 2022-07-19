#!/usr/bin/python3
"""Class square, it defines and compute square
properties
"""


class Square:
    """Defines a square with private field 'size'
    """

    def __init__(self, size=0):
        """ __init__ initialises the inputed parameters

        Args:
           size (int): The size of the sqaure

        """
        if (type(size) == int) and (size >= 0):
            self.__size = size
        elif type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Computes the area of a square
        Return: Area of square
        """
        return(self.__size**2)

    @property
    def size(self):
        """Getter for size attribute

        Returns:
           size atrribute
        """
        return(self.__size)

    @size.setter(self, size):
        """Setter for size attribute

        Args:
            __size : New value for size attribute

        Returns:
            Nothing
        """
        if (type(size) == int) and (size >= 0):
            self.__size = size
        elif type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
