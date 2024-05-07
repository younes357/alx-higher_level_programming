#!/usr/bin/python3
def pow(a, b):
    a1 = a
    for i in range(b - 1):
        a = a*a1
    return a
