#!/usr/bin/python3
"""Defining a class to raise an exception."""


class BaseGeometry:
    """defining a method to raise and Exception."""

    def area(self):
        """Not implemented Exception"""
        raise Exception("area() is not implemented")
