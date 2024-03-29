#!/usr/bin/python3
""" A Square module """


class Square:
    """ Declares a square class """

    def __init__(self, size=0) -> None:
        """
        Intializes the attributes
        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """ Fetch attribute to be used in the class """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be (less or equal to 0) >= 0")
        else:
            self.__size = value

    def area(self):
        """ Compute area for a square """
        return self.__size ** 2
