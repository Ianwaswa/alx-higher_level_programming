#!/usr/bin/python3
"""Checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """If the object is an instance of the class,
    return true; otherwise, return false
    """
    return (type(obj) == a_class)
