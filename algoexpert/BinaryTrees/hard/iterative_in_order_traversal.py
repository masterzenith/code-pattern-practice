"""
Iterative In-order Traversal
Write a function that takes in a Binary Tree (where nodes have an additional pointer to their parent node) and traverses
it iteratively using the in-order tree-traversal technique; the traversal should specifically not use recursion. As the
tree is being traversed, a callback function passed in as an argument to the main function should be called on each node
(i.e., callback(currentNode)).

Each BinaryTree node has an integer value, a parent node, a left child node, and a right child node. Children nodes can
either be BinaryTree nodes themselves or None / null.
Sample Input:
tree =    1
       /     \
      2       3
    /       /   \
   4       6     7
     \
      9
callback = someCallback
Sample Output:
// The input callback will have been called in the following order:
callback(4)
callback(9)
callback(2)
callback(1)
callback(6)
callback(3)
callback(7)

Hints:
1. Start by realizing that in-order traversal always traverses left child nodes before parent nodes before right child
nodes. In other words, you will somehow have to traverse the entire left side of the input Binary Tree before calling the
input callback on the root node and before traversing the entire right side.
2. While each node in the input Binary Tree does have a "parent" property, allowing you to traverse your way back up the
tree if need be, the difficulty arises when you must choose which node to actually call the input callback on. For instance,
on your way back up the left side of the input tree, how do you know whether to traverse the right side of a node or to
keep going up? Is there something that you can keep track of in order to know which node to call the input callback back
on next at any time during the life of your algorithm?
3. Try keeping track of three nodes at all times: a current node (the node currently being traversed), a previous node
(the node traversed just before the current one), and a next node (the next node to be traversed). Determine which node
to traverse next and when to call the input callback on the current node by analyzing the previous node. For instance,
if the previous node is actually the current node's left child node, then you know that you must call the callback on the
current node and that you must then explore the right side of the current node before going back up. Figure out all the
possible scenarios, and develop an algorithm to handle all of these scenarios.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the number of nodes in the Binary Tree
"""


class BinaryTree:
    def __init__(self, parent, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right


def iterative_in_order_traversal(tree, callback):
    previous_node = None
    current_node = tree
    while current_node is not None:
        if previous_node is None or previous_node == current_node.parent:
            if current_node.left is not None:
                next_node = current_node.left
            else:
                callback(current_node)
                next_node = current_node.right if current_node.right else current_node.parent
        elif previous_node == current_node.left:
            callback(current_node)
            next_node = current_node.right if current_node.right else current_node.parent
        else:
            next_node = current_node.parent
        previous_node = current_node
        current_node = next_node


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2, 1)
    root.right = BinaryTree(3, 1)
    root.left.left = BinaryTree(4, 2)
    root.left.right = BinaryTree(5, 2)
    root.left.right.left = BinaryTree(7, 5)
    root.left.right.right = BinaryTree(8, 5)
    root.right.left = BinaryTree(6, 3)
    root.right.right = BinaryTree(7, 3)
    print(iterative_in_order_traversal(root, callback=4))


if __name__ == "__main__":
    main()

