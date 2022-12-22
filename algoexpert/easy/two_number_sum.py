"""
Two Number Sum
Understanding the problem
Given an array of distinct integers and an integer representing the target sum, we are asked to implement
a function that is going to find out whether there's a pair of numbers in the array that adds up to the target sum.
If such pair exists, return the pair in any order; otherwise return an empty array. We cannot add a number to itself to
get the target sum.
"""


# O(N) time and space
def two_number_sum(array, targetSum):
    if len(array) < 2:
        return []
    map = set()
    for x in array:
        if targetSum - x in map:
            return x, targetSum - x
        else:
            map.add(x)
    return []


if __name__ == '__main__':
    print(two_number_sum([1, 3, 4, 5], 7))
