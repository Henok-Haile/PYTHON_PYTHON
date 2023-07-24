#!/usr/bin/python3
# 100-singly_linked_list.py
# Henok H Ghebreweldi <henokhaile53@gmail>
"""Defines classes for singly-linked list."""


class Node:
    """Repesents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node.
        
        Args:
            data (int): The data of a new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the data of the Node.
        
        Raises:
            TypeError: If data is not integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node of the Node.
        
        Raises:
            TypeError: if next_node is not a node object or not None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node to the SinglyLinkedList.
        
        The node is inserted into the correct sorted postion list,
        in increasing order.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and 
                tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines the print() representation of a singly linked list."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(values))