"""
Given an array, find the sum of all numbers between the K1'th and K2'th smallest elements of that array.
Example 1:
I/P: [1, 3, 12, 5, 15, 11], and K1 = 3, K2 = 6
O/P: 23
Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming between 5 and 15 is
            23(11 + 12)

Example 2:
I/P: [3, 5, 8, 7], and K1 = 1, K2 = 4
O/P: 12
Explanation: The sum of the numbers between the 1st smallest number(3) and the 4th smallest number (8) is 12 (5+7).

Time: Since we need to put only the top k2 numbers in the max-heap at any time, the time complexity of the above algo
        will be O(N*logk2)
Space: The space complexity will be O(k2), as we need to store the smallest 'k2' numbers in the heap.
"""
from heapq import *


def find_sum_of_elements(nums, k1, k2):
    max_heap = []
    # keep smallest k2 numbers in the max heap
    for i in range(len(nums)):
        if i < k2 - 1:
            heappush(max_heap, -nums[i])
        elif nums[i] < -max_heap[0]:
            heappop(max_heap)  # as we are interested only in the smallest k2 numbers
            heappush(max_heap, -nums[i])
    # get the sum of numbers between k1 and k2 indices
    # these numbers will be at the top of the max heap
    element_sum = 0
    # sum next k2-k1-1 numbers
    for _ in range(k2-k1-1):
        element_sum += -heappop(max_heap)
    return element_sum


def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


if __name__ == "__main__":
    main()
