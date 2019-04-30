# linked_list.py
# Jacob Glines
# 2019.04.22
# This file creates a linked list and fills it with words, deletes some
# and then prints them out in order
#
# Usage:
# python3 linked_list.py

from cslinked_list import LinkedList

# Global Variables
STOP_WORDS = ['the', 'an', 'and', 'a']


def add_words(list, filename):
    """Add words to the list."""

    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                list.insert(word)


def create_list():
    """Create a singly linked list."""

    words_list = LinkedList()
    add_words(words_list, 'test.txt')
    return words_list


def delete_words(words_list):
    """Delete stop words from the singly linked list.

    Variables:
        words_list  :  A singly linked list
        STOP_WORDS  :  A list of strings to delete from the list
    """

    for word in STOP_WORDS:
        q = None
        p = words_list.head
        while p is not None:
            if p.name == word:
                if q is not None:
                    q.next = p.next
                else:
                    words_list.head = p.next
            q = p
            p = p.next


def do_single_linked_list():
    """Create a list, delete words, and then print it."""
    words_list = create_list()
    delete_words(words_list)
    print("\nWORD           COUNTER\n")
    words_list.print()


do_single_linked_list()
