#!/usr/bin/python3
"""Defining  BaseGeometry class."""


class BaseGeometry:
    """Method to raise not implemented exception"""
    def area(self):
        raise Exception("area() is not implemented")
    """Method to validate value attribute"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
