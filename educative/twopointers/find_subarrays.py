"""
Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less
than the target number.
Input: [2, 5, 3, 10], target=30
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Time: O(N^3)
    The main for loop managing the sliding window takes O(N) but creating subarrays can take up to O(N^2) in the worst
    Case. Therefore overall, our algorithm will take O(N^3)

Space:
Ignoring the space required for the output list, the algorithm runs in O(N) space which is used for the temp list
So, at most, we need space for O(N^2) output lists. At worst, each subarray can take O(N) space, so overall, our
algorithm's space complexity will be O(N^3)
"""
from collections import deque


def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1
            '''
            since the product of all numbers from left to right is less than the target therefore, all subarrays from 
            left to right will have a product less than the target too; to avoid duplicates, we will start with a subarray
            containing only arr[right] and then extend it.ÒÒÒ
            '''
        temp_list = deque()
        for i in range(right, left - 1, -1):
            temp_list.appendleft(arr[1])
            result.append(list(temp_list))
    return result


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


if __name__ == '__main__':
    main()
