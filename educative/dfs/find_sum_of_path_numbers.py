"""
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
Find the total sum of all the numbers represented by all paths.
I/P:             1
            /       \
            7       9
                /       \
                2       9
O/P: 408
Explanation: The sum of all path numbers: 17+192+199

Time: O(N), where 'N' is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N), this space will be used to store the recursion stack. The worst case will happen when the given tree is a
        LinkedList(every node has only one child).
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    return find_root_to_leaf_path_numbers(root, 0)


def find_root_to_leaf_path_numbers(current_node, path_sum):
    if current_node is None:
        return 0

    # calculate the path number of the current node
    path_sum = 10 * path_sum + current_node.val

    # if the current_node is a leaf, return the current path_sum
    if current_node.left is None and current_node.right is None:
        return path_sum

    # traverse the left and the right sub-tree
    return find_root_to_leaf_path_numbers(current_node.left, path_sum) + find_root_to_leaf_path_numbers(current_node.right, path_sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


if __name__ == "__main__":
    main()
