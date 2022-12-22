"""
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target
number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the
triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Input: [-2, 0, 1, 2], target = 2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Time: Sorting the array will take O(N*logN). Overall, the function will take O(NlogN + N^2), which is asymptotically
      equivalent to O(N^2)
Space: The above algorithm's space complexity will be O(N), which is required for sorting.
"""
import math


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_diff = math.inf
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:  # we've found a triplet with an exact sum
                return target_sum - target_diff   # return sum of all the numbers

            # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
            if abs(target_diff) < abs(smallest_diff) or (abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff):
                smallest_diff = target_diff   # save the closest and the biggest difference

            if target_diff > 0:
                left += 1   # we need a triplet with a bigger sum
            else:
                right -= 1   # we need a triplet with a smaller sum
    return target_sum - smallest_diff


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


if __name__ == '__main__':
    main()
