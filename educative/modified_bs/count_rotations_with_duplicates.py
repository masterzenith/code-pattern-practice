"""
Given an array of numbers which is sorted in ascending order and is rotated 'k' times around a pivot, find 'k'.
You can assume that the array does have duplicates.
I/P: [3, 3, 7, 3]
O/P: 3
Explanation: The array has been rotated 3 times.
Original array: 3, 3, 3, 7
Array after 3 rotations: 3, 3, 7, 3

Time: This algorithm will run most of the time in O(logN). However, since we only skip two numbers in case of
    duplicates instead of half of the numbers, the worst case time complexity will become O(N).
Space: The algo runs in constant space O(1).
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
        # this is the only difference from the previous solution
        # if numbers at indices start, mid and end are same, we can't choose a side
        # the best we can do is to skip one number from both ends if they are not the smallest number
        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            if arr[start] > arr[start + 1]:     # if element at start + 1 is not the smallest
                return start + 1
            start += 1
            if arr[end - 1] > arr[end]:     # if the element at end is not the smallest
                return end
            end -= 1
        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            # left side is sorted, so the pivot is on right side
            start = mid + 1
        else:
            # right side is sorted, so the pivot is on the left side
            end = mid - 1
    return 0    # the array has not been rotated


def main():
    print(count_rotations([3, 3, 7, 3]))


if __name__ == '__main__':
    main()
