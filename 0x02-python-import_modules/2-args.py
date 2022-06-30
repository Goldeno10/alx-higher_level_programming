#!/usr/bin/python3
import sys

arg_count = len(sys.argv) - 1

if __name__ ==  "__main__":
    if arg_count < 2:
        print("{} arguments.".format(arg_count))
    else:
        print("{} arguments:".format(arg_count))
        for i in range(arg_count):
            print("{}: {}".format(i+1, sys.argv[i + 1]))


