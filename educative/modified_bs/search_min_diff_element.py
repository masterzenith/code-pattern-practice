"""
Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference
with the given 'key'.

I/P: [4, 6, 10], key = 7
O/P: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array.

I/P: [4, 6, 10], key = 4
O/P: 4

Time: Since, we are reducing the search range by half at every step, this means the time complexity of our algo will be
    O(logN) where 'N' is the total elements in the given array.
Space: The algo runs in constant space O(1).
"""


def search_min_diff_element(arr, key):
    if key < arr[0]:
        return arr[0]
    n = len(arr)
    if key > arr[n - 1]:
        return arr[n - 1]
    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return arr[mid]

    # at the end of the while loop, 'start == end + 1'
    # we are not able to find the element in the given array
    # return the element which is closet to the 'key'
    if (arr[start] - key) < (arr[end] - key):
        return arr[start]
    return arr[end]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


if __name__ == "__main__":
    main()
