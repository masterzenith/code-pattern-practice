"""
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
I/P:    Sequence: [1, 9, 9]                                     1
                                                            /       \
                                                            7       9
                                                                /       \
                                                                2       9
O/P:   true
Explanation: The tree has a path 1 -> 9 -> 9

Time: O(N), where 'N' is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N), this space will be used to store the recursion stack. The worst case will happen when the given tree is a
        LinkedList(every node has only one child).
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    if not root:
        return len(sequence) == 0
    return find_path_recursive(root, sequence, 0)


def find_path_recursive(current_node, sequence, sequence_idx):
    if current_node is None:
        return False

    seq_len = len(sequence)
    if sequence_idx >= seq_len or current_node.val != sequence[sequence_idx]:
        return False

    # If the current_node is a leaf, add it is the end of the sequence, we have found a path!
    if current_node.left is None and current_node.right is None and sequence_idx == seq_len - 1:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return find_path_recursive(current_node.left, sequence, sequence_idx + 1) or \
           find_path_recursive(current_node.right, sequence, sequence_idx + 1)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


if __name__ == "__main__":
    main()
