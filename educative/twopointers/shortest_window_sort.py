"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
I/P: [1, 2, 5, 3, 7, 10, 9, 12]
O/P: 5
Explanation: we need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

I/P: [1, 3, 2, 0, -1, 7, 10]
O/P: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
"""
import math


def shortest_window_sort(arr):
    low, high = 0, len(arr) - 1
    # find the first number out of sorting order from the beginning
    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1
    if low == len(arr) - 1:     # if the array is sorted
        return 0

    # find the first number out of sorting order from the end
    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1

    # find the maximum and minimum of the subarray
    subarray_max = -math.inf
    subarray_min = math.inf
    for k in range(low, high + 1):
        subarray_max = max(subarray_max, arr[k])
        subarray_min = min(subarray_min, arr[k])

    # extend the subarray to include any number which is bigger than the minimum of the subarray
    while low > 0 and arr[low - 1] > subarray_min:
        low -= 1

    # extend the subarray to include any number which is smaller than the maximum  of the subarray
    while high < len(arr) - 1 and arr[high + 1] < subarray_max:
        high += 1
    return high - low + 1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([-3, 2, -1, 100]))


if __name__=="__main__":
    main()