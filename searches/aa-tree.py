#!/bin/env python3

from node import Node

class AA_Tree:
    root = None

    def __init__(self, node):
        self.root = node

    def skew(self):
        if None in [self.root, self.root.lft]:        # right rotation
            return self.root
        if self.root.lft.lvl != self.root.lvl:        # no need to skew (not overfull)
            return self.root
        lft           = self.root.lft                 # 3 steps of rotation
        self.root.lft = lft.rgt
        lft.rgt       = self.root
        return lft
    
    def split(self):
        if None in [self.root, self.root.rgt, self.root.rgt.rgt]:
            return self.root
        if self.root.rgt.rgt.lvl != self.root.lvl:
            return self.root
        rgt           = self.root.rgt
        self.root.rgt = rgt.lft
        rgt.lft       = self.root
        rgt.lvl      += 1
        return rgt
    
    def insert(self, key, val):
        if self.root is None:
            return Node(key, val)
        if self.root.key == key:
            self.root.val = val
        elif key < self.root.key:
            self.root.lft = Node.insert(self.root.lft, key, val)
        else:
            self.root.rgt = Node.insert(self.root.rgt, key, val)
        self.root = self.skew()                   # incase in reverse
        self.root = self.split()
        return self.root
# main block
if __name__ == '__main__':
    (a, b, c, d, e) = range(5)

    node = Node(d, d)
    Node.insert(node, b, b)
    Node.insert(node, e, e)
    Node.insert(node, a, a)

    aa = AA_Tree(node)
    on = aa.insert(c, c)                         # out node

    print(on.lft.rgt.value)

