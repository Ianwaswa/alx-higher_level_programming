#!/usr/bin/python3
"""Verifies whether the object is an instance 
of a class or one of its inherited classes.
"""


def is_kind_of_class(obj, a_class):
    """Returns true if the object is an instance of the specified class or
    a class inherited by the given class; otherwise, returns false
    """
    return (isinstance(obj, a_class))
