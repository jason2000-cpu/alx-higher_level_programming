#!/usr/bin/python3
"""A function to check if an object is an instance of the specified class."""


def is_same_class(obj, a_class):
    """Return True if obj is an instance of a_class otherwise return False."""
    return isinstance(obj, a_class)
