#!/usr/bin/python3
"""
"""


class MyList(list):
    """A subclass of list
    """

    def __init__(self):
        """Object initializer"""

        super().__init__(self)

    def print_sorted(self): 
        """Print a sorted list"""    
        print(sorted(self)
