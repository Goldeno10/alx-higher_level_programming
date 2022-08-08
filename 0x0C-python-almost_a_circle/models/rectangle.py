#!/usr/bin/python3
"""Contains the class Rectangle that inherits from Base
"""


from . import base


class Rectangle(base.Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The initializer function"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return (self.__width)

    @width.setter
    def width(self, w_val):
        """Setter for width"""
        if type(w_val) != int:
            raise TypeError("width must be an integer")
        if w_val <= 0:
            raise ValueError("width must be > 0")
        self.__width = w_val

    @property
    def height(self):
        """getter for height"""
        return (self.__height)

    @height.setter
    def height(self, h_val):
        """Setter for height"""
        if type(h_val) != int:
            raise TypeError("height must be an integer")
        if h_val <= 0:
            raise ValueError("height must be > 0")
        self.__height = h_val

    @property
    def y(self):
        """getter for y"""
        return (self.__y)

    @y.setter
    def y(self, y_val):
        """setter for y"""
        if type(y_val) != int:
            raise TypeError("y must be an integer")
        if y_val < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_val

    @property
    def x(self):
        """getter for x"""
        return (self.__x)

    @x.setter
    def x(self, x_val):
        """setter for x"""
        if type(x_val) != int:
            raise TypeError("x must be an integer")
        if x_val < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_val

    def area(self):
        """Returns the area value of the Rectangle
        instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """prints in stdout the Rectangle instance with
        the character #.
        """
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Update the class Rectangle  by Assigns
        an argument to each attribute
        """
        arg_list = ["id", "width", "height", "x", "y"]
        if len(args) > len(arg_list):
                raise NameError("too many arguments for update")
        if args is not None and 0 < len(args) <= len(arg_list):
            for i in range(len(arg_list)):
                setattr(self, arg_list[i], args[i])
        elif len(args) == 0 and kwargs is not None:
            if len(kwargs) > 0:
                for key in kwargs:
                    if key in arg_list:
                        setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation
        of a Rectangle
        """
        arg_list = ["id", "width", "height", "x", "y"]
        dict_rep = {k: getattr(self, k) for k in arg_list}
        return (dict_rep)

    def __str__(self):
        """Returns the string representation of and
        instance/object
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width,
            self.__height))
