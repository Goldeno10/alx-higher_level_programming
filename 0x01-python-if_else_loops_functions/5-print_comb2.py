#!/usr/bin/python3
for number in range(0, 100):
    print("{:0>2}".format(number), end=", " if number != 99 else "")
