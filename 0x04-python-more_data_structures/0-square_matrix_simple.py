#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for i in matrix:
        subres = list(map(lambda x: x*x, i))
        res.append(subres)
    return res
