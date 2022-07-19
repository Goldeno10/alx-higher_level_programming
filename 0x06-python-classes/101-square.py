#!/usr/bin/python3
"""Class square, it defines and compute square
properties
"""


class Square:
    """Defines a square with private field 'size'

    Attributes:
        __size (int): size of a side of the square
        __position: tuple of 2 positive integers

    """

    def __str__(self):
        str_rep = ""

        if self.size == 0:
            return str_rep

        for i in range(self.position[1]):
            str_rep += "\n"

        for i in range(0, self.size):
            for k in range(self.position[0]):
                str_rep += " "
            for j in range(self.size):
                str_rep += "#"
            if i is not (self.size - 1):
                str_rep += "\n"

        return str_rep

    def __init__(self, size=0, position=(0, 0)):
        """ __init__ initialises the inputed parameters

        Args:
           self.__size (int): The size of the sqaure
           self.__position(int, int): position attribute

        """
        self.__size = size
        self.__position = position

    def area(self):
        """Computes the area of a square

        Returns:
           Area of square
        """
        return(self.__size**2)

    @property
    def size(self):
        """Getter for size attribute

        Returns:
           size atrribute
        """
        return(self.__size)

    @size.setter
    def size(self, size):
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

    @property
    def position(self):
        """Retrieves property attribute

        Returns:
           property values.
        """
        return(self.__property)

    @position.setter
    def position(self, value):
        """Setter for position

        Args:
           values: A turple of 2 positive integers

        Returns:
           Nothing
        """
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], isinstance(value[1], int)):
                    if value[0] >=0 and value[1] >= 0:
                        self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """prints in stdout the square with the
        character #.
        if size is equal to 0, print an empty line

        Returns:
           Nothing
        """

        if self.__size == 0:
            print()
        else:
            for s in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for q in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
