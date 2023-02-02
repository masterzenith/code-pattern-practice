"""
Same BSTs
An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer in the array,
from left to right, into the BST.
Write a function that takes in two arrays of integers and determines whether these arrays represent the same BST. Note
that you're not allowed to construct any BSTs in your code.
A BST is a Binary Tree that consists only of BST nodes. A node is said to be a valid BST node if and only if it satisfies
the BST property: its value is strictly greater than the values of every node to its left; its value is less than or
equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None /
null.
Sample Input:
arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
Sample Output:
true // both arrays represent the BST below
         10
       /     \
      8      15
    /       /   \
   5      12    94
 /       /     /
2       11    81

Hints:
1. You can immediately conclude that the input arrays don't represent the same BST if their first values aren't equal to
each other, since their first values represent the root of the BST. Similarly, you can conclude this if their lengths are
different. If their first values are equal to each other and their lengths are the same, what should your next step be?
2. Given an array of integers, all of the values in the array that are smaller than the first value in the array are
located in the left subtree of the BST that the array represents, and all of the values in the array that are greater
than or equal to the first value in the array are located in the right subtree of the BST that the array represents. Use
this fact and Hint #1 to recursively determine whether all subtrees in the BSTs represented by the arrays are equal to
each other.
3. Write a recursive function that takes in two arrays of integers. If the first values of the arrays aren't equal to
each other or if the arrays don't have the same length, the arrays don't represent the same BST. If the first values and
lengths are equal to each other, respectively, perform the following actions on both arrays: gather all integers that are
smaller than the first integer; these form a new array that represents the left subtree of the relevant BST; gather all
integers that are greater than or equal to the first integer; these form a new array that represents the right subtree of
the relevant BST. Call the recursive function twice: once with the two left-subtree arrays and once with the two
right-subtree arrays.
4. Do you actually need to create all of the auxiliary arrays mentioned in Hint #3?

Optimal Space & Time Complexity
O(n^2) time | O(d) space - where n is the number of nodes in each array, respectively, and d is the depth of the BST
that they represent
"""


def same_bsts(array_one, array_two):
    return are_same_bsts(array_one, array_two, 0, 0, float('-inf'), float('inf'))


def are_same_bsts(array_one, array_two, root_idx_one, root_idx_two, min_val, max_val):
    if root_idx_one == -1 or root_idx_two == -1:
        return root_idx_two == root_idx_two

    if array_one[root_idx_one] != array_two[root_idx_two]:
        return False

    left_root_idx_one = get_idx_of_first_smaller(array_one, root_idx_one, min_val)
    left_root_idx_two = get_idx_of_first_smaller(array_two, root_idx_two, min_val)
    right_root_idx_one = get_idx_of_first_bigger_or_equal(array_one, root_idx_one, max_val)
    right_root_idx_two = get_idx_of_first_bigger_or_equal(array_two, root_idx_two, max_val)

    current_value = array_one[root_idx_one]
    left_are_same = are_same_bsts(array_one, array_two, left_root_idx_one, left_root_idx_two, min_val, current_value)
    right_are_same = are_same_bsts(array_one, array_two, right_root_idx_one, right_root_idx_two, current_value, max_val)
    return left_are_same and right_are_same


def get_idx_of_first_smaller(array, starting_idx, min_val):
    for i in range(starting_idx + 1, len(array)):
        if array[starting_idx] > array[i] >= min_val:
            return i
    return -1


def get_idx_of_first_bigger_or_equal(array, starting_idx, max_val):
    for i in range(starting_idx + 1, len(array)):
        if array[starting_idx] <= array[i] < max_val:
            return i
    return -1


def main():
    arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    print(same_bsts(arrayOne, arrayTwo))


if __name__ == "__main__":
    main()
