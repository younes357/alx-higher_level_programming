#!/usr/bin/python3
def uppercase(str):
    x = []
    for i in range(len(str)):
        x.append(ord(str[i]))
        if i < len(str) - 1:
            if x[i] <= 122 and x[i] >= 97:
                x[i] = ord(str[i]) - 32
            print("{}".format(chr(x[i])), end="")
        elif i >= (len(str) - 1):
            if x[i] <= 122 and x[i] >= 97:
                x[i] = ord(str[i]) - 32
            print("{}".format(chr(x[i])))
