"""
Given a binary tree, find its maximum depth(or height).

I/P:        12
        /       \
        7       1
            /       \
            10      5
O/P: Maximum Depth: 3

Time: O(N), where N is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N) to store the nodes at each level in queue.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_max_depth(root):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    max_depth = 0
    while queue:
        max_depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()
            # insert the children of current node in the queue
            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)
    return max_depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Maximum Depth: " + str(find_max_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Maximum Depth: " + str(find_max_depth(root)))


if __name__ == "__main__":
    main()
