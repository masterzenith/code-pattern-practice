"""
BST Construction
Write a BST class for a Binary Search Tree. The class should support:
- Inserting values with the insert method.
- Removing values with the remove method; this method should only remove the first instance of a given value.
- Searching for values with the contains method.
Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single-node
tree should simply not do anything.
Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if
and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its
value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes
themselves or None / null.

Sample Usage
// Assume the following BST has already been created:
         10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14

// All operations below are performed sequentially.
insert(12):   10
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /        /  \
     1        12  14

remove(10):   12
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /           \
     1            14

contains(15): true

Hints:
1. As you try to insert, find, or a remove a value into, in, or from a BST, you will have to traverse the tree's nodes.
The BST property allows you to eliminate half of the remaining tree at each node that you traverse: if the target value
is strictly smaller than a node's value, then it must be (or can only be) located to the left of the node, otherwise it
must be (or can only be) to the right of that node.
2. Traverse the BST all the while applying the logic described in Hint #1. For insertion, add the target value to the BST
once you reach a leaf (None / null) node. For searching, if you reach a leaf node without having found the target value
that means the value isn't in the BST. For removal, consider the various cases that you might encounter: the node you
need to remove might have two children nodes, one, or none; it might also be the root node; make sure to account for
all of these cases.
3. What are the advantages and disadvantages of implementing these methods iteratively as opposed to recursively?

Optimal Space & Time Complexity
Average (all 3 methods): O(log(n)) time | O(1) space - where n is the number of nodes in the BST Worst (all 3 methods):
O(n) time | O(1) space - where n is the number of nodes in the BST
"""


class BST:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = self.right = None

    def insert(self, value):
        if not self:
            return BST(value)
        current = self
        while current:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = BST(value)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = BST(value)
                    break
        return self

    def contains(self, value):
        current = self
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value

    def remove(self, value, parent=None):
        if value < self.value:
            if self.left:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.get_min()
                self.right.remove(self.value, self)
            elif self.left is None and self.right is None:
                if not parent:
                    pass
                else:
                    if parent.left == self:
                        parent.left = None
                    else:
                        parent.right = None
            elif self.left is None:
                if not parent:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    if parent.left == self:
                        parent.left = self.right
                    else:
                        parent.right = self.right
            else:
                if not parent:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                else:
                    if parent.left == self:
                        parent.left = self.left
                    else:
                        parent.right = self.left


def main():
    root = BST(10)
    root.left = BST(5)
    root.right = BST(15)
    root.left.left = BST(2)
    root.left.right = BST(5)
    root.left.left.left = BST(1)
    root.right.left = BST(13)
    root.right.right = BST(22)
    root.right.left.right = BST(14)
    print(root.insert(12))
    print(root.contains(15))
    print(root.remove(10))


if __name__ == "__main__":
    main()