"""
Given an unsorted array of numbers, find the 'K' largest numbers in it.
Note: for a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

Example 1:
I/P: [3, 1, 5, 12, 2, 11], K = 3
O/P: [5, 12, 11]

Example 2:
I/P: [5, 12, 11, -1, 12], K = 3
O/P: [12, 11, 12]

Time:  As discussed above, the time complexity of this algorithm is O(K*logK + (N-K)*logK), which is asymptotically
        equal to O(N*logK)
Space: The space complexity will be O(K) since we need to store the top 'K' numbers in the heap.
"""
from heapq import *


def find_k_largest_numbers(nums, k):
    min_heap = []
    # put first 'K' numbers in the min heap
    for i in range(k):
        heappush(min_heap, nums[i])

    # go through the remaining numbers of the array, if the number from the array is bigger than the top(smallest)
    # number of the min_heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])

    # the heap has the top 'K' numbers, return them in a list

    return list(min_heap)


def main():
    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))
    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


if __name__ == "__main__":
    main()
