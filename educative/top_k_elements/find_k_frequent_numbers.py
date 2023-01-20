"""
Given an unsorted array of numbers, find the top 'K' frequently occurring numbers in it.
Example 1:
I/P: [1, 3, 5, 12, 11, 12, 11], K = 2
O/P: [12, 11]
Explanation: Both '11' and '12' appeared twice.

Example 2:
I/P: [5, 12, 11, 3, 11], K = 2
O/P: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.

Time: The time complexity of the above algorithm is O(N + N*logK)
Space: The space complexity will be O(N). Even though we are storing only 'K' numbers in the heap. For the frequency
        map, however, we need to store all the 'N' numbers.
"""
from heapq import *


def find_k_frequent_numbers(nums, k):
    # find the frequency of each number
    num_frequency_map = {}
    for num in nums:
        num_frequency_map[num] = num_frequency_map.get(num, 0) + 1
    min_heap = []

    # go through all numbers of the num_frequency_map and push them in the min_heap, which will have
    # top k frequent numbers. If the heap size is more than k, we remove the smallest(top) number
    for num, frequency in num_frequency_map.items():
        heappush(min_heap, (frequency, num))
        if len(min_heap) > k:
            heappop(min_heap)

    # create a list of top k numbers
    top_numbers = []
    while min_heap:
        top_numbers.append(heappop(min_heap)[1])
    return top_numbers


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


if __name__ == "__main__":
    main()
