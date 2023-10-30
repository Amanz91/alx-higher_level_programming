#!/usr/bin/python3
"""This a module that defines node of a singly
linked list.
"""


class Node:
    """Represents node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Intilizes a new node.
        Args:
            data (int): an integer stored in node.
            next_node (Node): the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the node."""
        return (self.__data)

    @data.setter
    def next_node(self, value):
        """Sets the data of the node.
        Args:
            value (int): integer value to store.
        Raises:
            TypeError: if value isn't integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node in the list"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the value of next node.
        Args:
            value (Node or none): a node object.
        Raises:
            TypeError: if not a Node object/ none
        """

        if not isinstance(value, Node) and
        value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This a class that defines a singly linked
    list.
    """

    def __init__(self):
        """Intializes a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node to the singly linked list.
        The list will be sorted in increasing order.
        Args:
            value (Node): the new node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            new2 = self.__head
            while (new2.next_node is not None and
                    new2.next_node.data < value):
                new2 = new2.next_node
            new.next_node = new2.next_node
            new2.next_node = new

    def printll(self):
        sll = []
        temp = self.__head
        while temp is not None:
            sll.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(sll))
