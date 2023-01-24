"""
For More details:
https://github.com/masterzenith/problemsolving/blob/main/src/pythonImage/ToplogicalSort/toplogicalSort11.pdf

Given an unsorted array of numbers, find Kth smallest number in it.
Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.
Example 1:
I/P: [1, 5, 12, 2, 11, 5], K = 3
O/P: 5
Explanation: The 3rd smallest number is '5'. as the first two smallest numbers are [1, 2]

Example 2:
I/P: [1, 5, 12, 2, 11, 5], K = 4
O/P: 5
Explanation: The 4th smallest number is '5', as the first three smallest numbers are [1, 2, 5].

Time: The time complexity of the above algorithm is O(K*logK + (N-K)*logK) which is asymptotically equal to O(N*logK).
Space: The space complexity will be O(K) because we need to store 'K' smallest numbers in the heap.

Similar Problem:
1. Find the Kth largest number in an unsorted array.
2. Find the median of an unsorted array.
3. Find the 'K' smallest or largest numbers in an unsorted array.
"""
from heapq import *


def find_kth_smallest_number(nums, k):
    max_heap = []
    # put first k numbers in the max heap
    for i in range(k):
        heappush(max_heap, -nums[i])

    # go through the remaining numbers of the array, if the number from the array is smaller than the top(biggest)
    # number of the heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if -nums[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
    # the root of the heap has the Kth smallest number
    return -max_heap[0]


def main():
    print("Kth smallest number: " +
          str(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))
    print("Kth smallest number: " +
          str(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))


if __name__ == "__main__":
    main()
