"""
Given a binary tree, populate an array to represent its level-by-level reverse order. i.e., the lowest level comes first
 You should populate the values of all
nodes of each level from left to right in separate sub-arrays.
Input:     1
        /   \
        2   3
       / \  /\
       4 5 6 7

Output: [[9, 10, 5], [7, 1], [12]]

Time: O(N), where N is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N) to store the nodes at each level in queue.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def reverse_traverse(root):
    result = deque()
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
        result.appendleft(current_level)
        # result = list(result)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse Level order traversal" + str(reverse_traverse(root)))


if __name__ == "__main__":
    main()
