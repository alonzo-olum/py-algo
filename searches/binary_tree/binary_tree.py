#!/bin/env python3

from tree_node import TreeNode

class BinaryTree:
    def __init__(self, node):
        self.tree_node = node

    #factory method creates a Singleton instance
    @classmethod
    def init(cls, value, left=None, right=None):
        node = TreeNode(value, left, right)
        return cls(node)

    def search(self, value):
        def traverse(node):
            if node is None or node.value == value:
                return node
            elif node.value < value:
                traverse(node.right_child)
            else:
                traverse(node.left_child) 
        return traverse(self.tree_node)

    def insert(self, value):
        def insert_or_traverse(node):
            if node.value < value:
                if node.right_child is None:
                    node.right_child = TreeNode(value)
                else:
                    insert_or_traverse(node.right_child)
            elif node.value > value:
                if node.left_child is None:
                    node.left_child = TreeNode(value)
                else:
                    insert_or_traverse(node.left_child)
        return insert_or_traverse(self.tree_node)

    def delete(self, value):
        def delete_or_traverse(node):
            def lift(successor_node):
                #current successor_node has no left_child
                #return right_child as successor successor_node
                if successor_node.left_child is None:
                    node.value = successor_node.value
                    return successor_node.right_child
                else:
                    #we keep traversing the left_child successor_nodes
                    successor_node.left_child = lift(successor_node.left_child)
                    return successor_node

            #begining of main closure
            #base case we are at the bottom of tree
            if node is None:
                return None
            #if value is less/greater than current node.
            #we set left/right children respectively
            elif node.value < value:
                node.right_child = delete_or_traverse(node.right_child)
                return node
            elif node.value > value:
                node.left_child = delete_or_traverse(node.left_child)
                return node
            #we found the deleted node
            #we return either of the child
            elif node.value == value:
                if node.left_child is None:
                    return node.right_child
                elif node.right_child is None:
                    return node.left_child
                #the deleted node has two children
                else:
                    node.right_child = lift(node.right_child)
                    return node
        return delete_or_traverse(self.tree_node)

#main block
btree = BinaryTree.init(50)
print(btree.tree_node.value)

node = btree.search(50)
print(node.value)

btree.insert(75)
print(btree.tree_node.right_child.value)

#delete is best illustrated from the './binary_tree_test.py'
del_node = btree.delete(75)
print(del_node.value)
