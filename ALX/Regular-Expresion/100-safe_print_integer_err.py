#!/usr/bin/python3
# 100-safe_print_integer_err.py
# Henok H Ghebreweldi <henokhaile53@gmail.com>

import sys
def safe_print_integer_err(value):
    """Prints an integer with "{:d}.format().

    If a value message is caught, a corresponding message is printed to standard error.

    Args:
        value (int): the integer to be printed.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr))
        return (False)