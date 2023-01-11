"""
Given a binary tree and a number 'S', find if the tree has a path from root-to-leaf such that the sum of all the node
values of that path equals 'S'.
I/P: S: 10
O/P: true
        1
    /       \
    2       3
/   \      / \
4   5     6   7
Explanation: The path with sum '10' is highlighted

Time: O(N), where 'N' is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N). This space will be used to store the recursion stack. The worst case will happen when the given tree is a
    LinkedList(every node has only one child)
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    if root is None:
        return False

    # if the current node is a leaf and its value is equal to the sum, we've found a path
    if root.val == sum and root.left is None and root.right is None:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


if __name__ == "__main__":
    main()
