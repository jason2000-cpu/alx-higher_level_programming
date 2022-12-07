#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = []
    uniq_add = 0
    for i in my_list:
        if i not in uniq_list:
            uniq_add += i
            uniq_list.append(i)

    return uniq_add
