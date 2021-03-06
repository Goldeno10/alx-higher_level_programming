#!/usr/bin/python3
"""This module contains a class Rectangle
"""


class Rectangle:
    """A Rectangle class for drawing a rectangle
    """

    def __init__(self, width=0, height=0):
        """The __init__ method for initializing the
        attributes

        Args:
            width (int): Rectangle width
            height (int): Rectangle height

        Returns:
            Nothing
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for wdth attribute
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Setter fot width
        Arg:
            value (int): New width parameter
        Returns:
            Nothing
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Getter for height attribute
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Setter fot height
        Arg:
            value (int): New height parameter
        Returns:
            Nothing
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
