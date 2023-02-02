"""
Compare Leaf Traversal
Write a function that takes in the root nodes of two Binary Trees and returns a boolean representing whether their leaf
traversals are the same.
The leaf traversal of a Binary Tree traverses only its leaf nodes from left to right. A leaf node is any node that has
no left or right children.
For example, the leaf traversal of the following Binary Tree is 1, 3, 2.
   4
 /   \
1     5
    /   \
   3     2
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null.

Sample Input:
tree1 = 1
      /   \
     2     3
   /   \     \
  4     5     6
      /   \
     7     8
tree2 = 1
      /   \
     2     3
   /   \    \
  4     7    5
            /  \
           8    6
Sample Output:
true
Hints:
1. To traverse the leaf nodes of a tree from left to right, you'll need to use a pre-order traversal.
2. The simplest approach to solving this problem is to perform a pre-order traversal on both trees, to store their leaf
nodes in arrays in the order in which they're visited, and to then compare the two resulting arrays. This solutions works,
but it's not optimal from a space-complexity perspective. Can you think of a way to solve this problem using less extra
space? It's possible to solve this with O(h1 + h2) space or better, where h1 is the height of tree1 and h2 is the height
of tree2.
3. To solve this problem with a more optimal space complexity, you can perform pre-order traversals on both trees at the
same time. As you traverse the trees, you need to look for the next leaf node in each tree and pause the traversal as soon
as you find it. Once you've found the next leaf node in both trees, you can compare their values and see if they match;
if they do, continue the traversal , and repeat the process. If they don't match, the leaf traversals aren't the same,
and you can return false.
4. Another unique way to solve this problem is to connect all of the leaf nodes in each individual tree so as to form two
linked lists. Since the leaf nodes don't have any children, you can use their right pointers to store the next leaf nodes
in the leaf traversals. And since you're reusing the input trees to store the leaf traversals, the only extra space you'll
be using comes from the recursion used in the traversal of the trees. Once both trees have their leaf nodes connected,
you can iterate through the linked lists and check if they're the same. To compare the linked lists, you'll need to keep
track of their heads (the first leaf node in each tree).

Optimal Space & Time Complexity
O(n + m) time | O(max(h1, h2)) space - where n is the number of nodes in the first Binary Tree, m is the number in the
second, h1 is the height of the first Binary Tree, and h2 is the height of the second
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def compare_leaf_traversal(tree1, tree2):
    list1, _ = connect_leaf_nodes(tree1)
    list2, _ = connect_leaf_nodes(tree2)

    current1 = list1
    current2 = list2
    while current1 is not None and current2 is not None:
        if current1.value != current2.value:
            return False
        current1 = current1.right
        current2 = current2.right
    return current1 is None and current2 is None


def connect_leaf_nodes(current_node, head=None, previous_node=None):
    if current_node is None:
        return head, previous_node
    if is_leaf_node(current_node):
        if previous_node is None:
            head = current_node
        else:
            previous_node.right = current_node
        previous_node = current_node
    leaf_head, left_previous_node = connect_leaf_nodes(current_node.left, head, previous_node)
    return connect_leaf_nodes(current_node.right, leaf_head, left_previous_node)


def is_leaf_node(node):
    return node.left is None and node.right is None


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.left.right.left = BinaryTree(7)
    root.left.right.right = BinaryTree(8)
    root.right.right = BinaryTree(6)
    root1 = BinaryTree(1)
    root1.left = BinaryTree(2)
    root1.right = BinaryTree(3)
    root1.left.left = BinaryTree(4)
    root1.left.right = BinaryTree(7)
    root1.right.right = BinaryTree(5)
    root1.right.right.left = BinaryTree(8)
    root1.right.right.right = BinaryTree(6)
    print(compare_leaf_traversal(root, root1))


if __name__ == "__main__":
    main()
