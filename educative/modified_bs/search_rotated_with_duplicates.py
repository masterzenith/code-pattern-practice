"""
Given an array of numbers has duplicates which is sorted in ascending order and also rotated by some arbitrary number,
find if a given 'key' is present in it.
Write a function to return the index of the 'key' in the rotated array. If the 'key' is not present, return -1. You can
assume that the given array does not have any duplicates.

I/P: [3, 7, 3, 3, 3], key = 7
    Original array: [3, 3, 3, 3, 7]
    Array after 2 rotations: [3, 7, 3, 3, 3]
O/P: 1
Explanation: '7' is present in the array at index '1'.

Time: This algorithm will run most of the time in O(logN). However, since we only skip two numbers in case of
    duplicates instead of half of the numbers, the worst case time complexity will become O(N).
Space: The algo runs in constant space O(1).
"""


def search_rotated_with_duplicates(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid

        # the only difference from the previous solution,
        # if numbers at indexes start, mid and end are same, we can't choose a side
        # The best we can do, is to skip one number from both ends as key != arr[mid]
        if arr[start] == arr[mid] and arr[mid] == arr[end]:
            start += 1
            end -= 1
        elif arr[start] <= arr[mid]:  # left side is sorted in ascending order
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
    print(search_rotated_with_duplicates([3, 7, 3, 3, 3], 7))


if __name__ == "__main__":
    main()
