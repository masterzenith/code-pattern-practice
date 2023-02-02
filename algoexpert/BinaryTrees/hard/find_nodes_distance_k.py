"""
Find Nodes Distance K
You're given the root node of a Binary Tree, a target value of a node that's contained in the tree, and a positive
integer k. Write a function that returns the values of all the nodes that are exactly distance k from the node with
target value.
The distance between two nodes is defined as the number of edges that must be traversed to go from one node to the other.
For example, the distance between a node and its immediate left or right child is 1. The same holds in reverse: the
distance between a node and its parent is 1. In a tree of three nodes where the root node has a left and right child,
the left and right children are distance 2 from each other.
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null.
Note that all BinaryTree node values will be unique, and your function can return the output values in any order.

Sample Input
tree = 1
     /   \
    2     3
  /   \     \
 4     5     6
           /   \
          7     8
target = 3
k = 2

Sample Output:
[2, 7, 8] // These values could be ordered differently.

Hints:
1. Would it be easier to solve this problem if you had information about every node's parent node?
2. One approach to this problem is to find the parent nodes of all nodes in the tree. With this information you can
perform a breadth-first search starting at the target node and traverse through each neighbor (left, right, and parent
node) of every node, keeping track of your distance from the target node at each iteration. Once you reach a node that
is distance k from the target node, you can add it to your output array. You'll have to also keep track of which nodes
you've visited so as to avoid visiting the same nodes over and over again.
3. Another approach is to use a recursive depth-first-search algorithm as follows:
    Case #1: when currentNode == target, search the subtree rooted at currentNode for all nodes that are k distance from
            currentNode.
    Case #2: when target is in the left subtree of currentNode at distance L + 1, look for nodes that are distance
            k - L - 1 in the right subtree of currentNode.
    Case #3: when target is in the right subtree of currentNode at distance L + 1, do the same thing as in case #2 but
            in the opposite subtree.
    Case #4: when target is neither in the left nor in right subtree of currentNode, stop recursing.

Optimal Space & Time Complexity
O(n) time | O(n) space - where n is the number of nodes in the tree
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_nodes_distance_k(tree, target, k):
    nodes_distance_k = []
    find_distance_from_node_to_target(tree, target, k, nodes_distance_k)
    return nodes_distance_k


def find_distance_from_node_to_target(node, target, k, nodes_distance_k):
    if node is None:
        return -1

    if node.value == target:
        add_subtree_nodes_at_distance_k(node, 0, k, nodes_distance_k)
        return 1
    left_distance = find_distance_from_node_to_target(node.left, target, k, nodes_distance_k)
    right_distance = find_distance_from_node_to_target(node.right, target, k, nodes_distance_k)

    if left_distance == k or right_distance == k:
        nodes_distance_k.append(node.value)

    if left_distance != -1:
        add_subtree_nodes_at_distance_k(node.right, left_distance + 1, k, nodes_distance_k)
        return left_distance + 1

    if right_distance != -1:
        add_subtree_nodes_at_distance_k(node.left, right_distance + 1, k, nodes_distance_k)
        return right_distance + 1
    return -1


def add_subtree_nodes_at_distance_k(node, distance, k, nodes_distance_k):
    if node is None:
        return

    if distance == k:
        nodes_distance_k.append(node.value)
    else:
        add_subtree_nodes_at_distance_k(node.left, distance + 1, k, nodes_distance_k)
        add_subtree_nodes_at_distance_k(node.right, distance + 1, k, nodes_distance_k)


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.left.left = BinaryTree(7)
    root.right.left.right = BinaryTree(8)
    print(find_nodes_distance_k(root, 3, 2))


if __name__ == "__main__":
    main()
