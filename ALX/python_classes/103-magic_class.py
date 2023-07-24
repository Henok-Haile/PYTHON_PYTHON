#!python3
# 103-magic_class.py
# Henok H Ghebreweldi <henokhaile53@gmail.com>
"""Defines a MagicClass excatly macthes a bytecode given."""

import math


class MagicClass:
    """Represents a circle."""
    
    def __init__(self, radius=0):
        """Initializes a MagicClass.
        
        Args:
            radius (float || int): Radius of the new MagicClass.

        Raises:
            TypeError: If radius is not integer or float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the are of the MagicClass."""
        return (self.__radius ** 2 * math.pi)
    
    def circumference(self):
        """Returns the circumference of the MagicClass."""
        return (2 * self.__radius * math.pi)