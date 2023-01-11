#!/usr/bin/python3
"""checks if object is a sub class of the specified class"""


def is_kind_of_class(obj, a_class):
    """
    Args:
       obj (any): The object to check
       a_class (type): The class to match the type of obj to.
    Returns:
       If obj is an instance or inherited instance of a_class -True
       Otherwise - False
    """
    
    """Return True is obj is a subclass if a_class"""
    if  isinstance(obj, a_class):
        return True
    return False









a = 2.3
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))