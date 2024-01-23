#!/usr/bin/python3
""" This is a square module """

class Square:
    """ Declare square class """

    def __init__(self, size) -> None:
        """
        Initialize class attribute
        Args:
            size: size of square
        """
        self.__size = size
