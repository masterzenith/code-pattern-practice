"""
Given 'M' sorted arrays, find the smallest range that includes at least one number from each of the 'M' lists.
Example 1:
I/P: L1= [1, 5, 8], L2 = [4, 12], L3=[7, 8, 10]
O/P: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3

I/P: L1=[1, 9], L2=[4, 12], L3=[7, 10,16]
O/P: [9, 12]
Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.

Time: Since, at most, we'll be going through all the elements of all the arrays and will remove/add one element in the
    heap in each step, the time complexity of the above algorithm will be O(N*logM) where 'N' is the total number of
    elements in all the 'M' input arrays.

Space: The space complexity will be O(M) because, at any time, our min-heap will be store one number from all the 'M'
        input arrays.
"""
from heapq import *
import math


def find_smallest_range(lists):
    min_heap = []
    range_start, range_end= 0, math.inf
    current_max_number = -math.inf

    # put the 1st element of each array in the max heap
    for arr in lists:
        heappush(min_heap, (arr[0], 0, arr))
        current_max_number = max(current_max_number, arr[0])

    # take the smallest(top) element from the min heap, if it gives us smaller range, update the ranges
    # if the array of the top element has more elements, insert the next element in the heap
    while len(min_heap) == len(lists):
        num, i, arr = heappop(min_heap)
        if range_end - range_start > current_max_number - num:
            range_start = num
            range_end = current_max_number
        if len(arr) > i + 1:
            # insert the next element in the heap
            heappush(min_heap, (arr[i+1], i + 1, arr))
            current_max_number = max(current_max_number, arr[i+1])
    return [range_start, range_end]


def main():
    print("Smallest range is: " +
          str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


if __name__ == "__main__":
    main()
