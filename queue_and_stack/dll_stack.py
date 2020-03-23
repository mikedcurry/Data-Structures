import sys
import os

dll_path = os.path.normpath(os.path.join(__file__, "../../doubly_linked_list"))
sys.path.append(dll_path)

# sys.path.append('doubly_linked_list\doubly_linked_list.py')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
        # self.size = 0 # WHY??????????

    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_from_tail()

    def len(self):
        return len(self.storage)
