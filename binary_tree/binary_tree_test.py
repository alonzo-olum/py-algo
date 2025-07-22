#!/bin/env python3

import unittest

from binary_tree import BinaryTree

class BinaryTreeTest(unittest.TestCase):

    def setUp(self):
        self.btree = BinaryTree.init(50)
        self.btree.insert(75)

    def tearDown(self):
        def zero_memory(root):
            if root.left_child is not None:
                zero_memory(root.left_child)
            elif root.right_child is not None:
                zero_memory(root.right_child)
            else:
                root = None

        zero_memory(self.btree.tree_node)

    def test_delete_raises_attr_error_deleted_value(self):
        self.btree.delete(75)
        with self.assertRaises(AttributeError):
            self.btree.tree_node.right_child.value

if __name__ == '__main__':
    unittest.main()
