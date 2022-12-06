#!/usr/bin/python3

def search_replace(my_list, search, replace):
    #my_list_cpy = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = 89

    return my_list
