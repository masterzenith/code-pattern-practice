"""
Max Path Sum In Binary Tree
Write a function that takes in a Binary Tree and returns its max path sum.
A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes; a path sum
is the sum of the values of the nodes in a particular path.
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null.

Sample Input:
tree = 1
    /     \
   2       3
 /   \   /   \
4     5 6     7

Sample Output:
18 // 5 + 2 + 1 + 3 + 7

Hints:
1. If you were to imagine each node in a Binary Tree as the root of the Binary Tree, temporarily eliminating all the
nodes that come above it, how would you find the max path sum for each of these newly imagined Binary Trees? In simpler
terms, how can you find the max path sum for each subtree in the Binary Tree?
2. For every node in a Binary Tree, there are four options for the max path sum that includes its value: the node's value
alone, the node's value plus the max path sum of its left subtree, the node's value plus the max path sum of its right
subtree, or the node's value plus the max path sum of both its subtrees.
3. A recursive algorithm that computes each node's max path sum and uses it to compute its parents' nodes' max path sums
seems appropriate, but realize that you cannot have a path going through a node and both its subtrees as well as that
node's parent node. In other words, the fourth option mentioned in Hint #2 poses a challenge to implementing a recursive
algorithm that solves this problem. How can you get around it?

Optimal Space & Time Complexity
O(n) time | O(log(n)) space - where n is the number of nodes in the Binary Tree
"""


class TreeInfo:
    def __init__(self):
        self.max_path_sum_using_current_node = 0
        self.max_path_sum = float('-inf')


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_path_sum(tree):
    root = calculate_max_path_sum(tree)
    return root[1]


def calculate_max_path_sum(node):
    if not node:
        return [0, float('-inf')]

    left_sub_tree = calculate_max_path_sum(node.left)
    right_sub_tree = calculate_max_path_sum(node.right)
    left_path_sum = left_sub_tree[0] + node.value
    right_path_sum = right_sub_tree[0] + node.value
    max_path_sum_using_current_node = max(left_path_sum, right_path_sum)
    current_max_path_sum = left_path_sum + right_path_sum - node.value
    max_path_sum_from_subtrees = max(left_sub_tree[1], right_sub_tree[1])
    max_path_sum = max(current_max_path_sum, max_path_sum_from_subtrees, max_path_sum_using_current_node)
    return [max_path_sum_using_current_node, max_path_sum]


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print(max_path_sum(root))


if __name__ == "__main__":
    main()
