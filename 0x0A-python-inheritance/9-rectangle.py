#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Method that returns the area of the
        instance"""
        return self.__width * self.__height

    def __str__(self):
        """ Special method that returns the printable
        string """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
