"""
Right Sibling Tree
Write a function that takes in a Binary Tree, transforms it into a Right Sibling Tree, and returns its root.
A Right Sibling Tree is obtained by making every node in a Binary Tree have its right property point to its right sibling
instead of its right child. A node's right sibling is the node immediately to its right on the same level or None / null
if there is no node immediately to its right.
Note that once the transformation is complete, some nodes might no longer have a node pointing to them. For example, in
the sample output below, the node with value 10 no longer has any inbound pointers and is effectively unreachable.
The transformation should be done in place, meaning that the original data structure should be mutated (no new structure
should be created).
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null.
Sample Input
tree =     1
      /         \
     2           3
   /   \       /   \
  4     5     6     7
 / \     \   /     / \
8   9    10 11    12 13
           /
          14
Sample Output
         1 // the root node with value 1
      /
     2-----------3
   /           /
  4-----5-----6-----7
 /           /     /
8---9    10-11    12-13 // the node with value 10 no longer has a node pointing to it
           /
          14
Hints:
1. Try to identify a pattern or formula that determines how to reach a given node's right sibling.
2. There are two patterns: if a node is the left child of another node, its right sibling is its parent's right child;
if a node is the right child of another node, its right sibling is its parent's right sibling's left child.
3. You'll need to a find a way to quickly access a node's parent's right child and a node's parent's right sibling; this
won't be trivial because the second one implies that the parent node's original right pointer has been overwritten.
4. Recursively traverse the binary tree and sequence the transformation operations as follows: at any given node, recursively
transform its left subtree into a right sibling tree, then edit the given node's right pointer to point to its right sibling,
and then finally recursively transform its right subtree into a right sibling tree. This sequencing of operations will
allow left child nodes to always access their parent's right child (before their parent's right pointer gets overwritten
to point to the parent's right sibling) and will allow right child nodes to always access their parent's right sibling
(after their parent's right pointer has gotten overwritten to point to the parent's right sibling).

Optimal Space & Time Complexity
O(n) time | O(d) space - where n is the number of nodes in the Binary Tree and d is the depth (height) of the Binary Tree
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def right_sibling_tree(root):
    mutate_help(root, None, None)
    return root


def mutate_help(node, parent, is_left_child):
    if node is None:
        return
    left, right = node.left, node.right
    mutate_help(left, node, True)
    if parent is None:
        node.right = None
    elif is_left_child:
        node.right = parent.right
    else:
        if parent.right is None:
            node.right = None
        else:
            node.right = parent.right.left
    mutate_help(right, node, False)


def main():
    binary_tree = BinaryTree(1)
    binary_tree.left = BinaryTree(2)
    binary_tree.right = BinaryTree(3)
    binary_tree.left.left = BinaryTree(4)
    binary_tree.left.right = BinaryTree(5)
    binary_tree.left.left.left = BinaryTree(8)
    binary_tree.left.left.right = BinaryTree(8)
    binary_tree.left.right.right = BinaryTree(10)
    print(right_sibling_tree(binary_tree))


if __name__ == "__main__":
    main()
