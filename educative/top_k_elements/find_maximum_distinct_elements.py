"""
Given an array of numbers and a number 'K', we need to remove 'K' numbers from the array such that we are left with
maximum distinct numbers.
Example 1:
I/P: [7, 3, 5, 8, 5, 3, 3] and K = 2
O/P: 3
Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have to skip 5 because
        it is not distinct and occurred twice. Another solution could be to remove one instance of '5' and '3' each to
        be left with three distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.

Example 2:
I/P: [3, 5, 12, 11, 12] and K = 3
O/P: 2
Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then we can delete any
        two numbers which will leave us 2 distinct numbers in the result.

Example 3:
I/P: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K = 2
O/P: 3
Explanation: We can remove one occurrence of '4' to get three distinct numbers.

Time: Since we will insert all numbers in a HashMap and a MinHeap, this will take O(N*logN) where 'N' is the total input
        numbers. While extracting numbers from the heap, in the worst case, we will need to take out 'K' numbers.
        This will happen when we have at least 'K' numbers with a frequency of two. Since the heap can have a maximum
        of 'N/2' numbers, therefore, extracting an element from the heap will take O(logN) and extracting 'K' numbers
        will take O(KlogN). So, overall, the time complexity of our algorithm will be O(N*logN + KlogN)

        we can optimize the above algorithm and only push 'K' elements in the heap, as in the worst case we will be
        extracting 'K' elements from the heap. This optimization will reduce the overall time complexity to
        O(N*logK + KlogK)
Space: The space complexity will be O(N) as, in the worst case, we need to store all the 'N' characters in the HashMap.
"""
from heapq import *


def find_maximum_distinct_elements(nums, k):
    distinct_element_count = 0
    if len(nums) <= k:
        return distinct_element_count

    # find the frequency of each number
    num_frequency_map = {}
    for i in nums:
        num_frequency_map[i] = num_frequency_map.get(i, 0) + 1

    min_heap = []
    # insert all numbers with frequency greater than '1' into the min_heap
    for num, frequency in num_frequency_map.items():
        if frequency == 1:
            distinct_element_count += 1
        else:
            heappush(min_heap, (frequency, num))

    # following a greedy approach, try removing the least frequent numbers first from the min_heap
    while k > 0 and min_heap:
        frequency, num = heappop(min_heap)
        # to make an element distinct, we need to remove all of its occurrences except obe
        k -= frequency - 1
        if k >= 0:
            distinct_element_count += 1

    # if k > 0, this means we have to remove some distinct numbers
    if k > 0:
        distinct_element_count -= k
    return distinct_element_count


def main():
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


if __name__ == "__main__":
    main()
