"""
Given an array 'arr' of unsorted numbers and a target sum, return all triplets in it such that
arr[i] + arr[j] + arr[k] < target where i, j and k are three different indices. Write a function to return the count of
such triplets.
Input: [-2, 0, 1, 2], target = 2
Output: [[-2, 0, 2], [-2, 0, 1], [-2, 1, 2]]
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Time: Sorting the array will take O(N*logN). Overall, the function will take O(NlogN + N^3), which is asymptotically
      equivalent to O(N^3)
Space: The above algorithm's space complexity will be O(N), which is required for sorting.
"""


def triplet_with_smaller_sum_list(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        search_pair(arr, target - arr[i], i, triplets)
    return triplets


def search_pair(arr, target_sum, first, triplets):
    left, right = first + 1, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target_sum:  # found the triplet
            # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
            # left and right to get a sum less than the target sum
            for i in range(right, left, - 1):
                triplets.append([arr[first], arr[left], arr[i]])
            left += 1
        else:
            right -= 1   # we need a pair with a smaller sum


def main():
    print(triplet_with_smaller_sum_list([-2, 0, 1, 2], 2))
    print(triplet_with_smaller_sum_list([-3, -1, 1, 2], -3))
    print(triplet_with_smaller_sum_list([1, 0, 1, 1], 100))


if __name__ == '__main__':
    main()
