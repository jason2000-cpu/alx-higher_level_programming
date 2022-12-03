#!/usr/bin/python3

def no_c(my_string):
    str = list(my_string)
    for i in range(0, len(str)):
        if str[i] == 'c' or str[i] == 'C':
            str[i] = ""
    return "".join(str)
