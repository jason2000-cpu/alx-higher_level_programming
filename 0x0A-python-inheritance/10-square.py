#!/usr/bin/python3
"""Defining the class Square which inherits from 9-rectangle.py"""
Rectangle = __import__('9-rectangle').Rectangle


def Square(Rectangle):
    """Initializing Square Class"""
    def __init__(self, size):
        """

        Args:
            size (int): square dimension
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
