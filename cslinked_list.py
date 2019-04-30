# cslinked_list.py
# Jacob Glines
# 2019.04.22
# This file defines a Linked list class with the usual behaviors
# of an linked list: print and insert
#
# Usage:
# from cslinked_list import LinkedList

from cslinked_list_node import LinkedListNode


class LinkedList:
    """ Implement a LinkedList object.

    The LinkedList class knows it's head. It also supports printing
    itself and inserting something into the list.
    """

    def __init__(self):
        self.head = None

    def print(self):
        """Travers/print items in the list."""

        p = self.head
        while p is not None:
            p.print()
            p = p.next

    def insert(self, value):
        """Insert a word into the tree in order.

        Variables:
            value  :  string to add to the list
        """

        p = self.head
        q = None
        done = False
        while not done:
            if self.head is None:
                self.head = LinkedListNode(value)
                p = self.head
                done = True
            elif p is None:
                t = LinkedListNode(value)
                p = t
                q.next = p
                done = True

            # We don't want the same word to print twice so we just
            # add to the counter.
            elif p.name == value:
                p.counter += 1
                done = True
            elif value < p.name:
                if self.head == p:
                    t = LinkedListNode(value)
                    t.next = p
                    self.head = t
                    done = True
                else:
                    t = LinkedListNode(value)
                    t.next = p
                    q.next = t
                    done = True
            q = p
            p = p.next



