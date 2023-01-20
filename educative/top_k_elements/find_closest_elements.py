"""
Given a sorted number array and two integers 'K' and 'X', find 'K' closest numbers to 'X' in the array. Return the
numbers in the sorted order. 'X' isn't necessarily present in the array.
Example 1:
I/P: [5, 6, 7, 8, 9], K = 3, X = 7
O/P: [6, 7, 8]

Example 2:
I/P: [2, 4, 5, 6, 9], K = 3, X = 6
O/P: [4, 5, 6]

Example 3:
I/P: [2, 4, 5, 6, 9], K = 3, X = 10
O/P: [5, 6, 9]

Time: The time complexity of the above algorithm is O(logN + K * logK). We need O(logN) for Binary Search and O(K*logK)
    to insert the numbers in the MinHeap, as well as to sort the output array.
Space: The space complexity will be O(K), as we need to put a maximum of 2K numbers in the heap.
"""
from heapq import *


def find_closest_elements_heap(arr, K, X):
    index = binary_search(arr, X)
    low, high = index - K, index + K
    low = max(low, 0)  # 'low' should not be less than zero
    # 'high' should not be greater the size of the array
    high = min(high, len(arr) - 1)
    min_heap = []
    # add all candidate elements to the min_heap, sorted by their absolute difference from 'X'
    for i in range(low, high + 1):
        heappush(min_heap, (abs(arr[i] - X), arr[i]))

    # we need the top 'K' elements having smallest difference from 'X'
    result = []
    for _ in range(K):
        result.append(heappop(min_heap)[1])
    result.sort()
    return result


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low > 0:
        return low - 1
    return low


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements_heap([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements_heap([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements_heap([2, 4, 5, 6, 9], 3, 10)))


if __name__ == "__main__":
    main()
