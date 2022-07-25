#!/usr/bin/python3
"""This module contains a class Rectangle
"""


class Rectangle:
    """A Rectangle class for drawing a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        x = cls(size, size)
        return x

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
        type(self).number_of_instances += 1

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
        """String representation of this class instance
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
            return string

    def __repr__(self):
        """String representation of class instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Class instance destructor method
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
