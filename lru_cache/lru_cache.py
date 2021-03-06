import sys
import os

dll_path = os.path.normpath(os.path.join(__file__, "../../doubly_linked_list"))
sys.path.append(dll_path)

# sys.path.append('doubly_linked_list\doubly_linked_list.py')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = DoublyLinkedList()
        self.dic = {} # this magic spot

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # check the dic, if not there return None
        if key in self.dic:
            # grab the node from the dic at the key
            node = self.dic[key]
            # since you're messing with it, bring it to the front in the list
            self.storage.move_to_front(node)
            # return the value from the dic -- position [1]
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # If the key already exists, delete it then add new as head
        if key in self.dic:
            self.storage.delete(self.dic[key])
        # If at the limit...
        elif len(self.storage) >= self.limit:
            # grab the node
            node = self.storage.remove_from_tail()
            # take the key out of the node and delete it from the dic
            del self.dic[node[0]]
        # add the new thing at the front of the list
        self.storage.add_to_head((key, value))
        # add the new thing to the dic
        self.dic[key] = self.storage.head
