# cslinked_list_node.py
# Jacob Glines
# 2019.04.22
# This file defines a Linked list node class with the usual behaviors
# of an node: the name, it's next (pointer), and the counter
#
# Usage:
# from cslinked_list_node import LinkedListNode


class LinkedListNode:
    """ Implement a LinkedListNode object.

    The LinkedListNode class supports a name, next, and counter. It also
    can print itself.
    """

    def __init__(self, value):
        self.name = value
        self.next = None
        self.counter = 1

    def print(self):
        """Print the name and counter."""

        print("{0:15}{1:4}".format(self.name, self.counter))


