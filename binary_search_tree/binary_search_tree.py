import os
import sys

path = os.path.normpath(os.path.join(__file__, '../../queue_and_stack'))
sys.path.append(path)

from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value to be inserted is >=
        if value >= self.value:
            # if something exist to the right --> recursion of insert...
            if self.right:
                # move right, recurse 'insert()'
                self.right.insert(value)
            # otherwise assign value at the empty spot to right
            else:
                self.right = BinarySearchTree(value)
        # else value must be smaller than compared to so move left...
        elif value < self.value:
            # same recursion as before but to the left
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base-case: the thing we're looking for is in front of us
        if target == self.value:
            return True
        # if target is smaller than value, then move left & recurse (if something there)
        elif target < self.value and self.left:
            return self.left.contains(target)
        # look right if target is bigger and recurse (if something is there)
        elif target > self.value and self.right:
            return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # apply function to current
        cb(self.value)
        # go left if possible and recurse
        if self.left:
            self.left.for_each(cb)
        # ALSO go right and recurse if possible
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go all the way to the left, then go one to the right
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Instantiate Queue
        q = Queue()
        # load the given binary tree instantiation into the queue
        q.enqueue(node)
        # Loop through the queue, removing values as I go, until empty
        while q.len():
            # Remove and print the current_node value
            c_node = q.dequeue()
            print(c_node.value)
            # add right child to queue
            if c_node.right:
                q.enqueue(c_node.right)
            # add left childe to queue
            if c_node.left:
                q.enqueue(c_node.left)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Instantiate Stack
        s = Stack()
        # put the current_node at top of stack
        s.push(node)
        # Loop through binary tree, stop when stack is empty
        while s.len():
            # much like bft, remove c_node from top and print it's value
            c_node = s.pop()
            print(c_node.value)
            # just like bft only with push
            if c_node.left:
                s.push(c_node.left)
            if c_node.right:
                s.push(c_node.right)



    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
