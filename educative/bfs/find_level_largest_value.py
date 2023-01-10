"""
Given a binary tree, find the largest value on each level of a binary tree.
I/P:
                    12
                 /      \
                7       1
            /   \      / \
            9   2     10  5
O/P: Level largest values: [12, 7, 10]

Time: O(N), where N is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N) to store the nodes at each level in queue.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        max_value = 0
        for _ in range(level_size):
            current_node = queue.popleft()
            # add the node's value to the running sum
            max_value = max(max_value, current_node.val)
            # insert the children of current_node to the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        # append the current_level's average to the result array
        result.append(max_value)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level's largest values are: " + str(find_level_averages(root)))


if __name__ == "__main__":
    main()
