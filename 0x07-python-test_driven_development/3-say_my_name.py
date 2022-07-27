#!/usr/bin/python3
"""This Module contains a function that
that take the first and last name as input
and prints an output

"""


def say_my_name(first_name, last_name=""):
    """say_name takes two string inputs one of which is op
    tional and give an output

    Args:
        first_name (str): fist input
        last_name (str): second input (optional)

    Returns:
        Nothing
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
