"""
Given an unsorted array of numbers and a target key, remove all instances of Key in-place and return the new length of
the array.
I/P: [3, 2, 3, 6, 3, 10, 9, 3], key=3
O/P: 4
Explanation: The first four elements after removing every 'key' will be [2, 6, 10, 9]

Time: O(N) where N is the total number of elements in the array
Space: O(1) cause, we don't need to use extra space
"""


def remove_element(arr, key):
    nextElement = 0  # Index of nextElement which is not 'key'
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1
    return nextElement


def main():
    print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(remove_element([4, 4, 4, 1], 4))


main()
