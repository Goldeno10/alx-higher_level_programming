#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrx = list(map(lambda it: [it[0]**2, it[1]**2, it[2]**2], matrix))
    return new_matrx
