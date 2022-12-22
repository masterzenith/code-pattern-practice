"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Have to return indices of the two numbers.
I/P: [1, 2, 3, 4, 6] target: 6
O/P: [1, 3]

Time: O(N) where n is the total number of elements in the given array.
Space: O(N) because in worst case it will push N elements to the HashTable
"""


def pair_with_targetsum(arr, target_sum):
    map = {}
    for i, num in enumerate(arr):
        diff = target_sum - arr[i]
        if diff in map:
            return [map[diff], i]
        else:
            map[arr[i]] = i
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
