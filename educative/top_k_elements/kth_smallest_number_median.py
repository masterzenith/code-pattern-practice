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

Time: Time complexity is O(N). Selection-based pivoting.
Space: The space complexity is O(N).

Similar Problem:
1. Find the Kth largest number in an unsorted array.
2. Find the median of an unsorted array.
3. Find the 'K' smallest or largest numbers in an unsorted array.
"""
from heapq import *


def find_kth_smallest_number(nums, k):
    return find_kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


def find_kth_smallest_number_rec(nums, k, start, end):
    p = partition(nums, start, end)

    if p == k - 1:
        return nums[p]

    if p > k  - 1:   # search lower part
        return find_kth_smallest_number_rec(nums, k, start, p - 1)

    # search higher part
    return find_kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, low, high):
    if low == high:
        return low

    median = median_of_medians(nums, low, high)
    # find the median in the array and swap it with 'nums[high]' which will become our pivot
    for i in range(low, high):
        if nums[i] == median:
            nums[i], nums[high] = nums[high], nums[i]
            break

    pivot = nums[high]
    for i in range(low, high):
        # all elements less than 'pivot' will be before the index 'low'
        if nums[i] < pivot:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
    # put the pivot in its correct place
    nums[low], nums[high] = nums[high], nums[low]
    return low


def median_of_medians(nums, low, high):
    n = high - low + 1
    # if we have less than 5 elements, ignore the partitioning algorithm
    if n < 5:
        return nums[low]

    # partition the given array into chunks of 5 elements
    partitions = [nums[j:j+5] for j in range(low, high+1, 5)]

    # for simplicity, lets ignore any partition with less than 5 elements
    full_partitions = [partition for partition in partitions if len(partition) == 5]

    # sort all partitions
    sorted_partitions = [sorted(partition) for partition in full_partitions]

    # find median of all partitions; the median of each partition is at index '2'
    medians = [partition[2] for partition in sorted_partitions]
    return partition(medians, 0, len(medians) - 1)


def main():
    print("Kth smallest number: " +
          str(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))
    print("Kth smallest number: " +
          str(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))


if __name__ == "__main__":
    main()
