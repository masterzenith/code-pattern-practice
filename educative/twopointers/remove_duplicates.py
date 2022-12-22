"""
Given an array of sorted numbers, remove all duplicates from it. After removing the duplicates in-place return the
length of the sub-array that has no duplicates in it.
I/P: [2, 3, 3, 3, 6, 9, 9]
O/P: 4

Time: O(N) where N is the total number of elements in the array
Space: O(1) Cause we don't need to store anything except defining some variables
"""


def remove_duplicates(arr):
    # index of nextNonDuplicateNumber
    next_non_duplicate_num = 1
    i = 1
    while i < len(arr):
        if arr[next_non_duplicate_num - 1] != arr[i]:
            arr[next_non_duplicate_num] = arr[i]
            next_non_duplicate_num += 1
        i += 1

    return next_non_duplicate_num


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([4, 4, 5, 5, 6]))


main()
