"""
Subtrees Within Range
Write a function that takes in a Binary Search Tree (BST) and a range of integers and returns the number of subtrees in
the BST that are only made up of nodes with values contained in the range.
For example, if the range is [10, 12], your function should return the number of subtrees in the BST that are only made
up of nodes with values 10, 11, or 12.
Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if
and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its
value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes
themselves or None / null.

Sample Input:
 tree =   10
        /     \
       5      15
     /   \   /   \
    2     8 13   22
  /      / \  \
 1      5   9  14
targetRange = [5, 15]
Sample Output:
 5
 // The 5 subtrees are:
 //   8    5    9    13    14
 //  / \               \
 // 5   9               14

Hints:
1. Can you come up with a recursive relation between whether a tree is within the target range and whether its subtrees
are within the range?
2. A tree is within the target range if its root node's value is within the range and if its left and right subtrees are
within the range.


"""


class BinaryTree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def count_subtrees_in_range(root, low, high):
#     count = [0]
#
#     def helper(node):
#         if not node:
#             return True
#         left_valid = helper(node.left)
#         right_valid = helper(node.right)
#         is_valid = left_valid and right_valid and low <= node.val <= high
#         if is_valid:
#             count[0] += 1
#         return is_valid
#
#     helper(root)
#     return count[0]


# def sub_trees_within_range(tree, target_range):
#     is_range_sub_trees = 0
#     is_bst_in_range(target_range, False, is_range_sub_trees)
#     return is_range_sub_trees
#
#
# def is_bst_in_range(target_range, in_range, in_range_sub_trees):
#     if tree is None:


def main():
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.right = BinaryTree(15)
    root.left.left = BinaryTree(2)
    root.left.right = BinaryTree(5)
    root.left.left.left = BinaryTree(1)
    root.right.left = BinaryTree(13)
    root.right.right = BinaryTree(22)
    root.right.left.right = BinaryTree(14)
    target_range = 12
