"""
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all
nodes of each level from left to right in separate sub-arrays.
Input:     1
        /   \
        2   3
       / \  /\
       4 5 6 7

Output: [[12], [7, 1], [9, 10, 5]]

Time: O(N), where N is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N) to store the nodes at each level in queue.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            # add the node to the current_level
            current_level.append(current_node.val)
            # insert current_level's children to the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal" + str(traverse(root)))


if __name__ == "__main__":
    main()
