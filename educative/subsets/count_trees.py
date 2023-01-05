"""
Count of structurally Unique Binary Search Trees(hard)
Given a number 'n', write a function to return the count of structurally unique BSTs that can store values 1 to 'n'.
I/P: 2
O/P: 2
Explanation: As we saw in the previous problem, there are 2 unique BSTs storing numbers from 1-2.

Time: The time complexity of the memoized algorithm will be O(n^2), since we are iterating from '1' to 'n' and
    ensuring that each sub-problem is evaluated only once.
Space: The space complexity will be O(n) for the hashmap that is used for memoization.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_trees(n):
    return count_trees_rec({}, n)


def count_trees_rec(map, n):
    if n in map:
        return map[n]

    if n <= 1:
        return 1
    count = 0
    for i in range(1, n+1):
        # making 'i' the root of the tree
        count_of_left_subtrees = count_trees_rec(map, i - 1)
        count_of_right_subtrees = count_trees_rec(map, n - i)
        count += (count_of_left_subtrees * count_of_right_subtrees)
    map[n] = count
    return count


def main():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


if __name__ == "__main__":
    main()