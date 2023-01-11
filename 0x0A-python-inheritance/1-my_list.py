#!/usr/bin/python3
"""This class inherits from class list and sorts a list in descending order"""


class MyList(list):
    """Initializing class MyList"""
    def __init__(self):
        pass
    """A method to sort the list tuple. It returns a sorted list"""
    def print_sorted(self, list):
        """ Try catch block to try for a non int value"""
        try:
            for i in range(len(list)):
                for j in range(len(list)):
                    if list[i] < list[j]:
                        temp = list[i]
                        list[i] = list[j]
                        list[j] = temp
        except TypeError:
            print("Not an int Tuple")

        return list
