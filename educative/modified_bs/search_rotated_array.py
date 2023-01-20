"""
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given
'key' is present in it.
Write a function to return the index of the 'key' in the rotated array. If the 'key' is not present, return -1. You can
assume that the given array does not have any duplicates.

I/P: [10, 15, 1, 3, 8], key = 15
    Original array: [1, 3, 8, 10, 15]
    Array after 2 rotations: [10, 15, 1, 3, 8]
O/P: 1
Explanation: '15' is present in the array at index '1'.

Time: Since, we are reducing the search range by half at every step, this means the time complexity of our algo will be
    O(logN) where 'N' is the total elements in the given array.
Space: The algo runs in constant space O(1).
"""


def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid

        if arr[start] <= arr[mid]:  # left side is sorted in ascending order
            if arr[start] <= key < arr[mid]:
                end = mid - 1
            else:   # key > arr[mid]
                start = mid + 1
        else:   # right side is sorted in ascending order
            if arr[mid] < key <= arr[end]:
                start = mid + 1
            else:   # key < arr[mid]
                end = mid - 1
    # we are not able to find the element in the given array
    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


if __name__ == "__main__":
    main()
