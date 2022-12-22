"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
I/P: [-3, 0, 1, 2, -1, 1, -2]
O/P: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Time: O(N^2) where N is the number of elements in the input array
Space: O(N) as for sorting array, we need N elements space.
"""


def search_triplets(arr):
    triplets = []
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:  # skip same element to avoid duplicate triplets
            continue
        search_pair(arr, -arr[i], i + 1, triplets)
    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with bigger sum
        else:
            right -= 1  # we need a pair with smaller sum


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))


if __name__ == '__main__':
    main()
