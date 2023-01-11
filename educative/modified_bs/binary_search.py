"""
Given a sorted array of numbers, find if a given number 'key' is present in the array. Though we know that the array
is sorted, we don't know if it's sorted in ascending or descending order. You should assume that the array can have
duplicates.
Write a function to return the index of the 'key' if it is present in the array, otherwise return -1.

I/P: [4, 6, 10], key = 10
O/P: 2

I/P: [1, 2, 3, 4, 5, 6, 7], key = 5
O/P: 4

Time: O(logN) where 'N' is the total elements in the given array. Since, we are reducing the search range by half at
    every step.
Space: This algo runs in constant space O(1).
"""


def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    is_ascending = arr[start] < arr[end]
    while start <= end:
        # calculate the middle of the current range
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return mid

        if is_ascending:    # ascending order
            if key < arr[mid]:
                end = mid - 1   # the 'key' can be in the first half
            else:
                start = mid + 1     # the 'key' can be in the second half
        else:   # descending order
            if key > arr[mid]:
                end = mid - 1   # the 'key' can be in the first half
            else:
                start = mid + 1     # the 'key' can be in the second half

    return -1  # key is not found!


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


if __name__ == "__main__":
    main()