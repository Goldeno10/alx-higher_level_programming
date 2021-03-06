#!/usr/bin/python3
"""Class square, it defines and compute square
properties
"""


class Square:
    """Defines a square with private field 'size'
    """

    def __init__(self, size):
        """ __init__ initialises the inputed parameters

        Args:
           size (int): The size of the sqaure

        """
        self.__size = size
