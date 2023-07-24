#!/usr/bin/python3
# 101-square.py
# Henok H Ghebreweldi <henokhaile53@gmail.com>
"""Defines a Square Class."""


class Square:
    """Represents a Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.
        
        Args:
            size (int): Size of the new square.
            position (int, int): Position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the current size of the square."""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        """Sets the current size of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the current postion of the square."""
        return (self.__position)
    @position.setter
    def position(self, value):
        """Sets the current position of the square.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or 
            not all(isinstance(num, int) for num in value) or 
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return (self.__size * self.__size)
    
    def my_print(self):
        """prints in stdout the square with the character #.
        if size is equal to 0, print an empty line."""
        if self.__size == 0:
            print()
            return
        
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
        
    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return("")