#!/usr/bin/python3
"""Return instance of a specific class."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given cls
    Args:
        obj (any): The object to check
        a_class (type): The cls to compare the type of obj to.
    Returns:
        Boolean of instance of a_class.
    """
    if type(obj) == a_class:
        return True
    return False
