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

# main block
if __name__ == '__main__':
    node = Node(8, 8)
    Node.insert(node, 4, 4)
    print(node.lft.value)
