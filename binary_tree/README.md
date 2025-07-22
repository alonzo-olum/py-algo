## Binary Tree

An illustration of how we can implement a binary tree.
A Binary Tree has the following properties:
	- Each Node has either zero, one or two children
	- If a node has two children, one is lesser than the parent while the other is greater than parent

### Building Blocks

 	- TreeNode Class
		- value: Int
		- left : TreeNode
		- right: TreeNode
	- BinaryTree Class
		- tree_node: TreeNode
		- methods:
			- search(value: Int)
			- insert(value: Int)
			- delete(value: Int)

### Testing

Nicely! written tests exemplifies what happens when you delete a node, then try accessing it.

## Running

Simply run the tests: `python3 binary_tree_test.py`

