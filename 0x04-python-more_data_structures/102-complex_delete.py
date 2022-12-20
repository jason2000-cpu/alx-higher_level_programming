#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    
    for i in range(len(a_dictionary)):
        if a_dictionary[i] == 'C':
            del a_dictionary[i]
        print(a_dictionary[i])
        
    # result = map(lambda x: list(map(lambda y: print(x[y]), x)), a_dictionary)
    print(list(result))
    
    
    
    
    
    
    
    





a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print(new_dict)
# print_sorted_dictionary(a_dictionary)
# print("--")
# print_sorted_dictionary(new_dict)

# print("--")
# print("--")
# new_dict = complex_delete(a_dictionary, 'c_is_fun')
# print_sorted_dictionary(a_dictionary)
# print("--")
# print_sorted_dictionary(new_dict)

    