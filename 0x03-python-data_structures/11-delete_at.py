#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list

    my_list_cpy = my_list.copy()
    my_list_cpy.remove(my_list_cpy[idx])
    return my_list_cpy
