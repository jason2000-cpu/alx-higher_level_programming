#!/usr/bin/python3
"""Defines a function to check for a sub class"""


def inherits_from(obj, a_class):
    """_summary_

    Args:
        obj (any): _description_
        a_class (class): _description_
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
