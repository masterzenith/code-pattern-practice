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

Solution: Binary Search -> Two Pointer
After finding the number closest to 'X' through Binary Search, we can use the Two Pointers approach to find the 'K'
closest numbers. Let's say the closest number is 'Y'. We can have a left pointer to move back from 'Y' and a right
pointer to move forward from 'Y'. At any stage, whichever number pointed out by the left or the right pointer gives
the smaller difference from 'X' will be added to our result list.
To keep the resultant list sorted we can use a Queue. So, whenever we take the number pointed out by the left pointer,
we will append it at the beginning of the list and whenever we take the number pointed out by the right pointer we will
append it at the end of the list.

Time: The time complexity of the above algorithm is O(logN + K). We need O(logN) for Binary Search and O(K) for finding
        the 'K' closest numbers using the two pointers.
Space: If we ignoring the space required for the output list, the algorithm runs in constant space O(1).
"""
from collections import deque


def find_closest_elements_heap(arr, K, X):
    result = deque()
    index = binary_search(arr, X)
    left_pointer, right_pointer = index, index + 1
    n = len(arr)
    for i in range(K):
        if left_pointer >= 0 and right_pointer < n:
            diff1 = abs(X - arr[left_pointer])
            diff2 = abs(X - arr[right_pointer])
            if diff1 <= diff2:
                result.appendleft(arr[left_pointer])
                left_pointer -= 1
            else:
                result.append(arr[right_pointer])
                right_pointer += 1
        elif left_pointer >= 0:
            result.appendleft(arr[left_pointer])
            left_pointer -= 1
        elif right_pointer < n:
            result.append(arr[right_pointer])
            right_pointer += 1
    return list(result)


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
