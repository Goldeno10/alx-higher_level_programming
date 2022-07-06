#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda it: [it[0]**2, it[1]**2, it[2]**2], matrix))
