"""
Given a binary tree and a number 'S', find all paths in the tree such that the sum of all the node values of each path
equals 'S'. Please note that the paths can start or end at any node but all paths must follow direction from parent to
child(top to bottom).

I/P: S: 12                              1
                                    /       \
                                    7       9
                                /      \   /    \
                                6       5 2     3
O/P: 3
Explanation: There are three paths with sum '12'.
7 -> 5, 1 -> 9 -> 2 and 9 -> 3

Time: O(N^2), where 'N' is the total number of nodes in the tree. This is due to the fact that we traverse each node
        once, but for every node, we iterate the current_path. The current_path in the worst case, can be O(N)
        (in the case of a skewed tree). But if the tree is balanced, then the current path will be equal to the height
        of the tree. O(logN). So the best case of our algorithm will be O(NlogN).
Space: O(N), this space will be used to store the recursion stack. The worst case will happen when the given tree is a
        LinkedList(every node has only one child).
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return count_paths_recursive(root, S, [])


def count_paths_recursive(current_node, S, current_path):
    if current_node is None:
        return 0

    # add the current_node to the path
    current_path.append(current_node.val)
    path_count, path_sum = 0, 0
    # find the sums of all sub-paths in the current_path list
    for i in range(len(current_path) - 1, -1, -1):
        path_sum += current_path[i]
        # if the sum of any sub-path is equal to 'S' we increment our path count
        if path_sum == S:
            path_count += 1

    # traverse the left sub-tree
    path_count += count_paths_recursive(current_node.left, S, current_path)
    # traverse the right sub-tree
    path_count += count_paths_recursive(current_node.right, S, current_path)

    # remove the current_node from the path to backtrack
    # we need to remove the current_node while we are going up the recursive call stack
    del current_path[-1]
    return path_count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


if __name__ == "__main__":
    main()
