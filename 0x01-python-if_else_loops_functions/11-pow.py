#!/usr/bin/python3
def pow(a, b):
    a1 = a
    if b > 0:
        for i in range(b - 1):
            a = a*a1
    elif and b < 0:
        for i in range(-b - 1):
            a = a*a1
        a = 1 / a
    return a
