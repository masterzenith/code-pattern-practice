"""
Given a binary tree, return an array containing nodes in its left view. The left view of a binary tree is the set of
nodes visible when the tree is seen from the left side.
Input:     1
        /   \
        2   3
       / \  /\
       4 5 6 7

Output:

Time: O(N), where N is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N) to store the nodes at each level in queue.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        for i in range(0, level_size):
            current_node = queue.popleft()
            # if it is the last node of this level, add it to the result
            result.append(current_node)
            # insert current_level's children to the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


if __name__ == "__main__":
    main()
