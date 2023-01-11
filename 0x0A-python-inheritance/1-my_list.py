#!/usr/bin/python3
"""This class inherits from class list and sorts a list in descending order"""


class MyList(list):
    """Initializing class MyList."""
    def __init__(self):
        pass
    """Print a list in sorted ascending order."""
    def print_sorted(self):
        return (sorted(self))
