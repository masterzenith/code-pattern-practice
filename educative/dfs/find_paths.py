"""
Given a binary tree and a number 'S', find all paths from root-to-leaf such that the sum of all the node values of each
path equals 'S'.

Input: S: 12
Output: 2
Explanation: There are the two paths with sum '12'.
1 -> 7 -> 4 and 1 -> 9 -> 2
                1
            /       \
            7       9
        /     \   /    \
        4     5   2    7

Time: O(N*logN) see https://github.com/masterzenith/problemsolving/blob/main/src/pythonImage/DFS/dfs3.pdf
Space: O(N*logN)


Similar Problems:
Problem1: Given a binary tree, return all root-to-leaf paths.
Solution: We can follow a similar approach. we just need to remove the "check for the path sum".

Problem2: Given a binary tree, find the root-to-leaf path with the maximum sum.
Solution: We need to find the path with the maximum sum. As we traverse all paths, we can keep track of the path with
        the maximum sum.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    all_paths = []
    find_paths_recursive(root, sum, [], all_paths)
    return all_paths


def find_paths_recursive(current_node, sum, current_path, all_paths):
    if current_node is None:
        return

    # add the current_node to the path
    current_path.append(current_node.val)

    # if the current_node is a leaf and its value is equal to sum, then save the current_path
    if current_node.val == sum and current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        # traverse the left sub-tree
        find_paths_recursive(current_node.left, sum - current_node.val, current_path, all_paths)
        # traverse the right sub-tree
        find_paths_recursive(current_node.right, sum - current_node.val, current_path, all_paths)

    # remove the current_node from the path to backtrack.
    # we need to remove the current_node while we are going up the recursive call stack.
    del current_path[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))


if __name__ == "__main__":
    main()
