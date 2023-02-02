"""
Validate BST
Write a function that takes in a potentially invalid Binary Search Tree (BST) and returns a boolean representing whether
the BST is valid. Each BST node has an integer value, a left child node, and a right child node. A node is said to be a
valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node
to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either
valid BST nodes themselves or None / null.
A BST is valid if and only if all of its nodes are valid BST nodes.
Sample Input
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14

Sample Output
true

Hints:
1. Every node in the BST has a maximum possible value and a minimum possible value. In other words, the value of any
given node in the BST must be strictly smaller than some value (the value of its closest right parent) and must be
greater than or equal to some other value (the value of its closest left parent).
2. Validate the BST by recursively calling the validateBst function on every node, passing in the correct maximum and
minimum possible values to each. Initialize those values to be -Infinity and +Infinity.

Optimal Space & Time Complexity
O(n) time | O(d) space - where n is the number of nodes in the BST and d is the depth (height) of the BST
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


def validate_bst(tree):
    return validate_bst_helper(tree, float('-inf'), float('inf'))


def validate_bst_helper(tree, min_value, max_value):
    if not tree:
        return True
    if not min_value <= tree.value < max_value:
        return False
    return validate_bst_helper(tree.left, min_value, tree.value) and \
           validate_bst_helper(tree.right, tree.value, max_value)


def main():
    root = BST(10)
    root.left = BST(5)
    root.right = BST(15)
    root.left.left = BST(2)
    root.left.right = BST(5)
    root.left.left.left = BST(1)
    root.right.left = BST(13)
    root.right.right = BST(22)
    root.right.left.right = BST(14)
    print(validate_bst(root))


if __name__ == "__main__":
    main()
