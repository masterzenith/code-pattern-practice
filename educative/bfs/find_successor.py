"""
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor
is the node that appears right after the given node in the level order traversal.

I/P: Given Node: 3
                1
            /       \
            2       3
        /       \
        4       5
O/P: Level order successor: 4

Time: O(N), where N is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N) to store the nodes at each level in queue.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    if root is None:
        return None

    queue = deque()
    queue.append(root)
    while queue:
        current_node = queue.popleft()
        # insert the children of current node in the queue
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        # break if we have found the key
        if current_node.val == key:
            break
    return queue[0] if queue else None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


if __name__ == "__main__":
    main()
