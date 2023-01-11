#!/usr/bin/python3

class MyList(list):
    def __init__(self):
        pass
    
    def print_sorted(self, list):
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
        
        
        
my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

print(my_list)
my_list.print_sorted(my_list)
print(my_list)
# list = [1, 0, 4, 3, 7, 12, 6]
# print(inst1.print_sorted(list))