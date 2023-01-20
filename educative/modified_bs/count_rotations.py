"""
Given an array of numbers which is sorted in ascending order and is rotated 'k' times around a pivot, find 'k'.
You can assume that the array does not have any duplicates.
I/P: [10, 15, 1, 3, 8]
O/P: 2
Explanation: The array has been rotated 2 times.
Original array: 1, 3, 8, 10, 15
Array after 2 rotations: 10, 15, 1, 3, 8

I/P: [4, 5, 7, 9, 10, -1, 2]
O/P: 5
Explanation: The array has been rotated 5 times.
Original array: -1, 2, 4, 5, 7, 9, 10
Array after 5 rotations: 4, 5, 7, 9, 10, -1, 2

I/P: [1, 3, 8, 10]
O/P: 0
Explanation: The array has not been rotated

Time: Since we are reducing the search range by half at every step, this means that the time complexity of our algo
    will be O(logN) where 'N' is the total elements in the given array.
Space: The algorithm runs in constant space O(1)
"""


def count_rotations(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2

        # if mid is greater than the next element
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        # if mid is smaller than the previous element
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid
        if arr[start] < arr[mid]:   # left side is sorted, so the pivot is on right side
            start = mid + 1
        else:
            # right side is sorted, so the pivot is on the left side
            end = mid - 1
    return 0    # the array has not been rotated


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


if __name__ == '__main__':
    main()
