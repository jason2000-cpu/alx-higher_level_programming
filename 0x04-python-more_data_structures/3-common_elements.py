#!/usr/bin/python3

def common_elements(set_1, set_2):
    sorted_list = []
    for i in set_1:
        for j in set_2:
            if i == j:
                sorted_list.append(j)

    return list(sorted_list)
