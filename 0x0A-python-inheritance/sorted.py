#!/usr/bin/python3

list = [1, 0, 4, 3, 7, 12, "String", 6]

def sortList(list):
    try:
        for i in range(len(list)):
            for j in range(len(list)):
           
                if list[i] > list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
    except TypeError:
        print("Not an int Tuple")

    return list
            

print(sortList(list))