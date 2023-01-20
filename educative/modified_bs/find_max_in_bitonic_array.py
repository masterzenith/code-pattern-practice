"""
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing
and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array
arr[i] != arr[i+1]

I/P: [1, 3, 8, 12, 4, 2]
O/P: 12
Explanation: The maximum number in the input bitonic array is '12'.

I/P: [10, 9, 8]
O/P: 10

Time: Since, we are reducing the search range by half at every step, this means the time complexity of our algo will be
    O(logN) where 'N' is the total elements in the given array.
Space: The algo runs in constant space O(1).
"""


def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    # at the end of the while loop, 'start == end'
    return arr[start]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


if __name__ == "__main__":
    main()