"""
Given an array of numbers sorted in ascending order, find the range of a given number 'key'. The range of the 'key' will
be the first and last position of the 'key' in the array.

Write a function to return the range of the 'key', if the 'key' is not present return [-1, -1].

I/P: [4, 6, 6, 6, 9], key = 6
O/P: [1, 3]

I/P: [1, 3, 8, 10, 15], key = 10
O/P: [3, 3]

Time: O(logN) where 'N' is the total elements in the given array. We are reducing the search range by half at every step.
Space: The algorithm runs in constant space O(1)
"""


def find_range(arr, key):
    result = [-1, -1]
    result[0] = binary_search(arr, key, False)
    if result[0] != -1:     # no need to search, if 'key' is not present in the inout array
        result[1] = binary_search(arr, key, True)
    return result


# modified Binary Search
def binary_search(arr, key, find_max_idx):
    key_idx = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:   # key == arr[mid]
            key_idx = mid
            if find_max_idx:
                start = mid + 1     # search ahead to find the last index of 'key'
            else:
                end = mid - 1   # search behind to find the first index of 'key'
    return key_idx


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


if __name__ == "__main__":
    main()
