#!/usr/bin/python3
# 101-safe_function.py
# Henok H Ghebreweldi <henokhaile53@gmail.com>

import sys

def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to be executed.
        args: Argguments of the fct.

    Returns:
         If an error occurs - None.
         Otherwise -The result of the call to the fct.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr))
        return (None)