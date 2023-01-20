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

Time: Since we need to put all the numbers in a min-heap, the time complexity of the above algorithm will be O(n*logn)
        where 'N' is the total input numbers
Space: The space complexity will be O(N), as we need to store all the 'N' numbers in the heap.
"""
from heapq import *


def find_sum_of_elements(nums, k1, k2):
    min_heap = []
    # insert all numbers to the min_heap
    for num in nums:
        heappush(min_heap, num)

    # remove k1 small numbers from the min_heap
    for _ in range(k1):
        heappop(min_heap)
    element_sum = 0
    # sum next k2-k1-1 numbers
    for _ in range(k2-k1-1):
        element_sum += heappop(min_heap)
    return element_sum


def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


if __name__ == "__main__":
    main()
