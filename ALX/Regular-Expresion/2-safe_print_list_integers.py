#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Henok H. Ghebreweldi <henokhaile53@gmail.com>


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list that are integers only.

    Args:
        my_list (list): The list from which elements to be printed.
        x (int): The number of elements of my_list to be printed.
    
        Returns:
            The number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print ("{:d}".format(my_list[i]), end="")
            ret += 1
        except (TypeError, ValueError):
            continue

    print()
    return (ret)
