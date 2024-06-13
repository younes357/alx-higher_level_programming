#!/usr/bin/python3
def uniq_add(my_list=[]):
    c = 0
    for i, e in enumerate(my_list):
        if my_list.index(e) == i:
            c += my_list[i]
        else:
            continue
    return c
