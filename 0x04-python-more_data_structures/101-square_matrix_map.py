#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    def sqr(it):
        a = it[0]**2
        b = it[1]**2
        c = it[2]**2
        return [a,b,c]
    new_matrx = list(map(sqr, matrix))
    return new_matrx
