#!/usr/bin/python3
"""Contain the class Square that inherits from Rectangle:
"""


from . import rectangle


class Square(rectangle.Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """The initializer function"""
        super().__init__(size, size, x, y, id)

    @rectangle.Rectangle.width.setter
    def width(self, w_val):
        """Setter for width"""
        super().width(w_val)
        super().height(w_val)

    @property
    def size(self):
        """getter for size"""
        return (self.width)

    @size.setter
    def size(self, s_val):
        """setter for size"""
        if type(s_val) != int:
            raise TypeError("width must be an integer")
        if s_val <= 0:
            raise ValueError("width must be > 0")
        self__width = s_val
        self.__height = s_val

    def update(self, *args, **kwargs):
        """Update the class Square  by Assigns
        an argument to each attribute:
        """
        arg_list = ["id", "size", "x", "y"]
        if args != None and len(args) > 0:
            for i in range(len(args)):
                setattr(self, arg_list[i], args[i])
        elif len(args) == 0 and kwargs != None:
            if len(kwargs) > 0:
                for key in kwargs:
                    if key in arg_list:
                        setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation
        of the object
        """
        arg_list = ["id", "size", "x", "y"]
        dict_rep = {k:getattr(self, k) for k in arg_list}
        return (dict_rep)

    def __str__(self):
        """Returns the string representation of and
        instance/object
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
            self.x, self.y, self.width))
