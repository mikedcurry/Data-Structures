import sys
import os

dll_path = os.path.normpath(os.path.join(__file__, "../../doubly_linked_list"))
sys.path.append(dll_path)

# sys.path.append('doubly_linked_list\doubly_linked_list.py')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        return self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_from_head()

    def len(self):
        return len(self.storage)
