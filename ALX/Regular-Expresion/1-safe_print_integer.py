#!usr/bin/python3
# 1-safe_print_integer.py
# Henok H Ghbereweldi <henokhaile53@gmail.com>


def safe_print_integer(value):
    """prints an integer with "{:d}".format().

    Args:
        value (int): The integer value to be printed.
    
    Returns:
        If a TypeError or ValueError occurs - False
        Otherwise - True
    """
    try:
        print ("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False