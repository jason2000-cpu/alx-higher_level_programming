#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of all available object's attributes"""
    return (dir(obj))
