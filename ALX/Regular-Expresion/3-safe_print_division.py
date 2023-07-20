#!/usr/bin/python3
# 3-safe_print_division.py
# Henok H Ghebreweldi <henokhaile53@gmail.com>


def safe_print_division(a, b):
    """Divides two Integers.
    
    Args:
        a (int): First integer Number - Dividend.
        b (int): Second integer Number - Divisor.
        
    Returns: The division of two integer numbers - Quotient.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)