#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None
    finally ZeroDivisionError:
        print("Inside result: {}".format(result))
        return (result)
