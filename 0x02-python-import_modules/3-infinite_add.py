#!/usr/bin/python3
import sys

arg_c = len(sys.argv) - 1
arg_v = sys.argv
if __name__ == "__main__":
    num = 0
    if arg_c > 0:
        for i in range(arg_c):
            num += int(arg_v[i+1])
    print(num)
