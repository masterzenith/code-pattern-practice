"""
Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest
path between any two leaf nodes. The diameter of a tree may or may not pass through the root.
Note: You can always assume that there are at least two leaf nodes in the given tree.

I/P:                1
                /       \
                2       3
                |   /       \
                4   5       6
O/P: output: 5
Explanation: The diameter of the tree is: [4, 2, 1, 3, 6]

Time: O(N), where 'N' is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space: O(N), this space will be used to store the recursion stack. The worst case will happen when the given tree is a
        LinkedList(every node has only one child).
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:
    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, current_node):
        if current_node is None:
            return 0

        left_tree_height = self.calculate_height(current_node.left)
        right_tree_height = self.calculate_height(current_node.right)

        # if the current_node doesn't have a left or right subtree, we can't have a path passing through it, since we
        # need a leaf node on each side
        if left_tree_height is not None and right_tree_height is not None:
            # diameter at the current_node will be equal to the height of left subtree +
            # the height of the right subtree + '1' for the current_node
            diameter = left_tree_height + right_tree_height + 1

            # update the global tree diameter
            self.treeDiameter = max(self.treeDiameter, diameter)

        # height of the current_node will be equal to the maximum of the heights of left or right subtrees plus '1' for
        # the current_node
        return max(left_tree_height, right_tree_height) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.left.right.right = TreeNode(10)
    root.right.right.right = TreeNode(9)
    root.right.right.right.right = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


if __name__ == "__main__":
    main()