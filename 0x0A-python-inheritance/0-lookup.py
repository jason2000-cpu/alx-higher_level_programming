#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """This function returns a list of all the available attributes and methods
    of the obj class"""
    return (dir(obj))
