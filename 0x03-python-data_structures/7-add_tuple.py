#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    
    if type(tuple_a) is int:
        tuple_a = (tuple_a, 0)

    if type(tuple_b) is int:
        tuple_b = (tuple_b, 0)
    
    if not tuple_a:
        tuple_a = (0, 0)

    if not tuple_b:
        tuple_b = (0,0)

    tupleList = []
    for i in range(2):
        tupleList.append(tuple_a[i] + tuple_b[i])

    return tuple(tupleList)



tuple_a = (1,)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, (1,))
print(new_tuple)

# print(add_tuple(tuple_a, (1, )))
# print(add_tuple(tuple_a, ()))