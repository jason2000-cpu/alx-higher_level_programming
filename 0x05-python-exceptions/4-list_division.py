#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Print x elememts of a list.
    Args:
        my_list_1 (list): The list to divide elements from.
        my_list_2 (list): The list to divide elements with
        list_length (int): The number of elements of  the both lists.
    Returns:
        The number of elements printed.
    """

    div_Arr = []
    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
            div_Arr.append(quotient)
        except TypeError:
            div_Arr.append(0)
            i += 1
            print("Wrong Type")
        except IndexError:
            div_Arr.append(0)
            print("out of range")
        except ZeroDivisionError:
            div_Arr.append(0)
            i += 1
            print("division by 0")

    return div_Arr
