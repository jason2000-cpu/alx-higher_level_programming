#!/usr/bin/python3

def search_replace(my_list, search, replace):
    my_list_cpy = my_list.copy()
    for i in range(len(my_list_cpy)):
        if my_list_cpy[i] == search:
            my_list[i] = replace

    return my_list_cpy
