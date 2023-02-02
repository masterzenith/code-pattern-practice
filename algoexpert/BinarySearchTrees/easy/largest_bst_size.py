"""
Largest BST Size
Write a function that takes in a Binary Tree and returns the size of the largest Binary Search Tree (BST) contained in it.
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null.
A BST is a special type of Binary Tree whose nodes all satisfy the BST property. A node satisfies the BST property if
its value is strictly greater than the values of every node to its left; its value is less than or equal to the values
of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

Sample Input:
tree =            20
          /                \
         7                 10
       /   \             /     \
      0     8           5      15
          /   \       /   \   /   \
         7     9     2     5 13   22
                   /           \
                  1             14
Sample Output
 9 // The subtree rooted at 10 is the largest BST in the tree, with 9 nodes.

Summary: https://github.com/lee-hen/Algoexpert/blob/master/assessments/07_largest_bst_size/summary.md
"""


class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def largest_bst_size(root):
#     def helper(node):
#         nonlocal max_size
#         if not node:
#             return float('inf'), float('-inf'), 0
#         left_min, left_max, left_size = helper(node.left)
#         right_min, right_max, right_size = helper(node.right)
#         if left_max < node.val < right_min:
#             size = left_size + right_size + 1
#             max_size = max(max_size, size)
#             return min(left_min, node.val), max(right_max, node.val), size
#         return float('-inf'), float('inf'), 0
#
#     max_size = 0
#     helper(root)
#     return max_size


def largest_bst_size(tree):
    validate_size = get_binary_tree_size(tree, 0)
    return validate_size


def get_binary_tree_size(tree, validate_size):
    if tree is None:
        return True, 0
    validate_left, left_size = get_binary_tree_size(tree.left, validate_size)
    validate_right, right_size = get_binary_tree_size(tree.right, validate_size)
    if validate_left:
        validate_size = max(validate_size, left_size)
    if validate_right:
        validate_size = max(validate_size, right_size)

    current_size = left_size + right_size + 1
    validate = False
    if tree.left is not None and tree.right is not None:
        if tree.left.value < tree.value <= tree.right.value:
            validate = True
    elif tree.left is not None:
        if tree.value > tree.left.value:
            validate = True
    elif tree.right is not None:
        if tree.value <= tree.right.value:
            validate = True
    else:
        validate = True
    validate_cur = validate and validate_left and validate_right
    if validate_cur:
        validate_size = max(validate_size, current_size)
    return validate_cur, current_size


def main():
    root = BinaryTree(20)
    root.left = BinaryTree(7)
    root.right = BinaryTree(10)
    root.left.left = BinaryTree(0)
    root.left.right = BinaryTree(8)
    root.left.right.left = BinaryTree(7)
    root.left.right.right = BinaryTree(9)
    root.right.left = BinaryTree(4)
    root.right.left.left = BinaryTree(2)
    root.right.left.right = BinaryTree(5)
    root.right.left.left.left = BinaryTree(1)
    root.right.left.right.left = BinaryTree(50)
    root.right.left.right.left.left = BinaryTree(60)
    root.right.right = BinaryTree(15)
    root.right.right.left = BinaryTree(13)
    root.right.right.left.right = BinaryTree(14)
    root.right.right.right = BinaryTree(22)
    print(largest_bst_size(root))


if __name__ == "__main__":
    main()
