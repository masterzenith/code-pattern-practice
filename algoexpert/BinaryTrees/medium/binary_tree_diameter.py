"""
Binary Tree Diameter
Write a function that takes in a Binary Tree and returns its diameter. The diameter of a binary tree is defined as the
length of its longest path, even if that path doesn't pass through the root of the tree.
A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes. The length
of a path is the number of edges between the path's first node and its last node.
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null.

Sample Input:
tree =        1
            /   \
           3     2
         /   \
        7     4
       /       \
      8         5
     /           \
    9             6
Sample Output:
6 // 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6
// There are 6 edges between the
// first node and the last node
// of this tree's longest path.

Hints:
1. How can you use the height of a binary tree and the heights of its subtrees to calculate its diameter?
2. The length of the longest path that goes through the root of a binary tree is the sum of the heights of its left and
right subtrees (left subtree height + right subtree height). The diameter of a binary tree can be calculated by taking
the maximum of: 1) the maximum subtree diameter (max(left subtree diameter, right subtree diameter)); and 2) the length
of the longest path that goes through the root (left subtree height + right subtree height).
3. Implement a variation of depth-first search that recursively keeps track of both the diameter and the height of a each
subtree in the input binary tree. Follow Hint #2 to continuously compute these diameters.

Optimal Space & Time Complexity
Average case: when the tree is balanced O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h
is the height of the Binary Tree
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_diameter(tree):
    longest_diameter = [0]
    binary_tree_helper(tree, longest_diameter)
    return longest_diameter[0]


def binary_tree_helper(tree, longest_diameter):
    if tree is None:
        return 0

    max_left_path = binary_tree_helper(tree.left, longest_diameter)
    max_right_path = binary_tree_helper(tree.right, longest_diameter)
    max_current_path_length = max_left_path + max_right_path
    longest_diameter[0] = max(longest_diameter[0], max_current_path_length)
    return max(1 + max_left_path, 1 + max_right_path)


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.left.right.left = BinaryTree(7)
    root.left.right.right = BinaryTree(7)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print(binary_tree_diameter(root))


if __name__ == "__main__":
    main()

