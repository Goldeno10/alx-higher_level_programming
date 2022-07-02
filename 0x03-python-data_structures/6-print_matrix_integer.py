#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for t in matrix:
        for i in t:
            print("{:d}".format(i), end=" " if t.index(i) < (len(t)-1) else "")
        print()
