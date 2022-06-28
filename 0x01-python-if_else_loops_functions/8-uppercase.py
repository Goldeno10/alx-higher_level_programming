#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(ord('a'), ord('z')):
            c = (chr(ord(c) - 32))
        print("{}".format(c), end = "")
    print("", end = "\n")

