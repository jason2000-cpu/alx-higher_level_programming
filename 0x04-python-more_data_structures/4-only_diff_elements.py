#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    joined_set = set_1.union(set_2)
    for i in set_1:
        for j in set_2:
            if i == j:
                joined_set.remove(i)

    return list(joined_set)
