#!/usr/bin/python3
# 4-list_division.py
# Henok H Ghebreweldi <henokhaile53@gmail.com>


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element of two lists.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): maximum length of the list

    Returns:
        A new list (length = list_length) containing all divisions.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)