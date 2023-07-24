#!/usr/bin/python3
# 5-square.py
# Henok H Ghebreweldi <henokhaile53@gmail.com>
"""Defines a Square Class."""


class Square:
    """Represents a Square class."""

    def __init__(self, size=0):
        """Initializes a new square.
        
        Args:
            size (int): Size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square."""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        """Sets the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return (self.__size * self.__size)
    
    def my_print(self):
        """prints in stdout the square with the character #.
        if size is equal to 0, print an empty line."""
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()