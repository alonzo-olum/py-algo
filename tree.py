#!/bin/env python3

from node import Node

class Tree:
    root = None
    def __setitem__(self, key, val):
        self.root = Node.insert(self.root, key, val)

    def __getitem__(self, key):
        return Node.search(self.root, key)

    def __contains__(self, key):
        try:
            Node.search(self.root, key)
        except KeyError:
            return False
        return True
# main block
if __name__ == '__main__':
    node = Node(8, 8)
    tr = Tree()
    tr[8] = 8
    node_tr = tr[8]
    print(node_tr.value)
