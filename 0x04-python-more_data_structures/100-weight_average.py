#!/usr/bin/python3

def weight_average(my_list=[]):
    summation = 0
    divident = 0
    for i in my_list:
        multiply = i[0] * i[1]
        divident += i[1]
        summation += multiply
        print(multiply)

    return summation/divident
