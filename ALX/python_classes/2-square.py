#!/usr/bin/python3
# 2-square.py
# Henok H Ghebreweldi <henokhaile53@gmail.com>
"""Defines a Square class."""


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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size