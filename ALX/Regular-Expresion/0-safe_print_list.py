#!/usr/bin/python3
# 0-safe_print_list.py
# Henok H Ghebreweldi <henokhaile53@gmail.com>

    
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.
    
    Args:
        my_list (list): The list from which the elements to be printed.
        x (int): The number of elements to be printed.code 
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print()
    return ret