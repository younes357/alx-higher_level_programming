#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    res1 = []
    res2 = []
    res = list(map(lambda x: x*x, matrix[0]))
    res1 = list(map(lambda x: x*x, matrix[1]))
    res2 = list(map(lambda x: x*x, matrix[2]))
    return [res, res1, res2]
