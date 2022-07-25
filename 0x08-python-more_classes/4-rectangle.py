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

    def area(self):
        """area:
        Returns:
             the area of a rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """perimeter:
        Returns:
            computes the perimeter of a
        rectangle
        """
        if (self.__height == 0) or (self.__width == 0):
            return (0)
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """returns printable string representation
        of the rectangle
        """

        string = ""
        if self.width == 0 or self.height == 0:
            return string

        for i in range(self.height):                                   string += ("#" * self.width) + "\n"

        return string[:-1]

    def __repr__(self):
        """String representation of class instance
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
