"""
All Kinds Of Node Depths
The distance between a node in a Binary Tree and the tree's root is called the node's depth.
Write a function that takes in a Binary Tree and returns the sum of all of its subtrees' nodes' depths.
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null.
Sample Input:
tree =    1
       /     \
      2       3
    /   \   /   \
   4     5 6     7
 /   \
8     9
Sample Output
26
// The sum of the root tree's node depths is 16.
// The sum of the tree rooted at 2's node depths is 6.
// The sum of the tree rooted at 3's node depths is 2.
// The sum of the tree rooted at 4's node depths is 2.
// Summing all of these sums yields 26.

Hints:
1. You can calculate the sum of a tree's node depths with a simple recursive function. Iterate through every node in the
tree, call the simple recursive function on each node to calculate the sum of the node depths of the tree rooted at the
node in question, and add up all the sums to obtain the final sum.
2. You can solve this question in linear time by coming up with a relation between a tree's sum of node depths and the
sums of node depths of the trees rooted at its left and right child nodes.
3. The depth of a node relative to a node X is 1 value smaller than its depth relative to node X's parent node Y. It
follows that, if a subtree rooted at node X has a sum of node depths S, you can get the sum of those node depths relative
to node Y by calculating: S + number-of-nodes-in-subtree-rooted-at-X, since this effectively increments all the node
depths relative to node X by 1.
4. From Hint #3, we can deduce the formula:
nodeDepths(node) = nodeDepths(node.left) + numberOfNodesInLeftSubtree + nodeDepths(node.right) + numberOfNodesInRightSubtree.
We can easily count the number of nodes in each subtree with a single pass in the input tree, and then we can apply this
formula to calculate all of the node depths in linear time and finally sum them up.

Optimal Space & Time Complexity
Average case: when the tree is balanced O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h
is the height of the Binary Tree

Notes:
https://github.com/lee-hen/Algoexpert/tree/master/very_hard/10_all_kinds_of_node_depths#notes
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, num_nodes_in_tree, sum_of_depths, sum_of_all_depths):
        self.num_nodes_in_tree = num_nodes_in_tree
        self.sum_of_depths = sum_of_depths
        self.sum_of_all_depths = sum_of_all_depths


def all_kinds_of_node_depths(root):
    return get_tree_info(root).sum_of_all_depths


def get_tree_info(tree):
    if tree is None:
        return TreeInfo(0, 0, 0)

    left_tree_info = get_tree_info(tree.left)
    right_tree_info = get_tree_info(tree.right)

    sum_of_left_depths = left_tree_info.sum_of_depths + left_tree_info.num_nodes_in_tree
    sum_of_right_depths = right_tree_info.sum_of_depths + right_tree_info.num_nodes_in_tree

    num_nodes_in_tree = 1 + left_tree_info.num_nodes_in_tree + right_tree_info.num_nodes_in_tree

    sum_of_depths = sum_of_left_depths + sum_of_right_depths
    sum_of_all_depths = sum_of_depths + left_tree_info.sum_of_all_depths + right_tree_info.sum_of_all_depths
    return TreeInfo(num_nodes_in_tree, sum_of_depths, sum_of_all_depths)


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.left.right.left = BinaryTree(7)
    root.left.right.right = BinaryTree(7)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print(all_kinds_of_node_depths(root))


if __name__ == "__main__":
    main()
