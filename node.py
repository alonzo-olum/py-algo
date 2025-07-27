#!/bin/env python3

class Node:
    lft = None
    rgt = None

    def __init__(self, key, val):
        self.key = key
        self.value = val

    @staticmethod
    def insert(node, key, val):
        if node is None: return Node(key, val)
        if node.key == key: node.val = val
        elif key < node.key:
            node.lft = Node.insert(node.lft, key, val)
        else:
            node.rgt = Node.insert(node.rgt, key, val)
        return node

    @staticmethod
    def search(node, key):
        if node is None: raise KeyError
        if node.key == key:
            return node
        elif node.key < key:
            return Node.search(node.rgt, key)
        else:
            return Node.search(node.lft, key)

# main block
if __name__ == '__main__':
    node = Node(8, 8)
    ret = Node.insert(node, 4, 4)
    print(ret.value)
    print(node.lft.value)
