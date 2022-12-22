"""
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the
target number.
I/P: [4, 1, 2, -1, 1, -3], target=1
O/P: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.

I/P: [2, 0, -1, 1, -2, 2], target=2
O/P: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.

Time: O(N^3)
Space: O(N) which is required for sorting
"""


def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []

    for i in range(0, len(arr) - 3):
        # skip same element to avoid duplicate quadruplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            #  skip same element to avoid duplicate quadruplets
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            search_pairs(arr, target, i, j, quadruplets)

    return quadruplets


def search_pairs(arr, target_sum, first, second, quadruplets):
    left = second + 1
    right = len(arr) - 1
    while left < right:
        quad_sum = arr[first] + arr[second] + arr[left] + arr[right]
        if quad_sum == target_sum:  # found the quadruplets
            quadruplets.append([arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate quadruplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate quadruplets
        elif quad_sum < target_sum:
            left += 1  # we need a pair with bigger sum
        else:
            right -= 1  # we need a pair with smaller sum


def main():
    arr = [2, 0, -1, 1, -2, 2]
    target = 2
    print(search_quadruplets(arr, target))
    arr = [4, 1, 2, -1, 1, 3]
    target = 1
    print(search_quadruplets(arr, target))


if __name__ == '__main__':
    main()
