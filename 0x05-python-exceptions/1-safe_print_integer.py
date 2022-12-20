#!/usr/bin/python3

def safe_print_integer(value):
    """Print x elememts of a list.
    Args:
        value (integer): the integer to print
    Returns:
        returns true if the value is an integer
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
