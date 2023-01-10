"""
Given a binary tree, connect each node with its level order successor. The last node of each level should point to the
first node of the next level.

I/P:            1 ->
            /       \
            2--->   3
        /   |     /  \
        4-> 5->  6-> 7 -> null
O/P: 12 -> 7 -> 1 -> 9 -> 10 -> 5 -> Null

Time: O(N), where N is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N) to store the nodes at each level in queue.
"""
from __future__ import print_function

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    current_node, previous_node = None, None
    while queue:
        current_node = queue.popleft()
        if previous_node:
            previous_node.next = current_node
        previous_node = current_node

        # insert the children of current node in the queue
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_tree()


if __name__ == "__main__":
    main()
