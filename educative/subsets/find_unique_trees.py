"""
Structurally Unique Binary Search Trees:
Given a number 'n', write a function to return all structurally unique Binary Search Trees(BST) that can store values
1 to 'n'

I/P: 2
O/P: List containing root nodes of all structurally unique BSTs.
Explanation: Here are the 2 structurally unique BSTs storing all numbers from 1 to 2: 1 --> 2 and 2 ---> 1

Can be solved with Memoization as well. However, the overall time complexity of the memoized algorithm will also be the
same.

Time: O(n*2^n)
Space: O(2^n)
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_unique_trees(n):
    if n <= 0:
        return []
    return find_unique_trees_rec(1, n)


def find_unique_trees_rec(start, end):
    result = []
    # base condition, return 'None' for an empty sub-tree
    # consider n = 1, in this case we will have start = end - 1, this means we should have only one tree
    # we will have two recursive calls, find_unique_trees_rec(1, 0) and (2, 1)
    # both of these should return 'None' for the left and the right child
    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        # making i the root of the tree
        left_sub_trees = find_unique_trees_rec(start, i - 1)
        right_sub_trees = find_unique_trees_rec(i + 1, end)
        for left_tree in left_sub_trees:
            for right_tree in right_sub_trees:
                root = TreeNode(i)
                root.left = left_tree
                root.right = right_tree
                result.append(root)
    return result


def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))


if __name__ == "__main__":
    main()
