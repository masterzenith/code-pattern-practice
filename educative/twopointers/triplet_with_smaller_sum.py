"""
Given an array 'arr' of unsorted numbers and a target sum, count all triplets in it such that
arr[i] + arr[j] + arr[k] < target where i, j and k are three different indices. Write a function to return the count of
such triplets.
Input: [-1, 0, 2, 3], target = 3
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Time: Sorting the array will take O(N*logN). Overall, the function will take O(NlogN + N^2), which is asymptotically
      equivalent to O(N^2)
Space: The above algorithm's space complexity will be O(N), which is required for sorting.
"""


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        count += search_pair(arr, target - arr[i], i)
    return count


def search_pair(arr, target_sum, first):
    count = 0
    left, right = first + 1, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target_sum:  # found the triplet
            # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
            # left and right to get a sum less than the target sum
            count += right - left
            left += 1
        else:
            right -= 1   # we need a pair with a smaller sum
    return count


def main():
    print(triplet_with_smaller_sum([-2, 0, 1, 2], 2))
    print(triplet_with_smaller_sum([-3, -1, 1, 2], -3))
    print(triplet_with_smaller_sum([1, 0, 1, 1], 100))


if __name__ == '__main__':
    main()
