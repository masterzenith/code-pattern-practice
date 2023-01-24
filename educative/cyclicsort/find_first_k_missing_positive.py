"""
Given an unsorted array containing numbers and a number 'k', find the first 'k' missing positive number in the array.
Example 1:
I/P: [3, -1, 4, 5, 5], k = 3
O/P: [1, 2, 6]
Explanation: The smallest missing positive number are 1, 2, 6.
Example 2:
I/P: [2, 3, 4], k = 3
O/P: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5, and 6.
Example 3:
I/P: [-2, -3, 4], k = 2
O/P: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.

Time: The time complexity of the above algorithm is O(n + k), as the last two for loops will run for O(n) and O(k)
        respectively.
Space: The algorithm needs O(k) space to store the extra_numbers.
"""


def find_first_k_missing_positive(nums, k):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]     # swap
        else:
            i += 1
    missing_numbers = []
    extra_numbers = set()
    for i in range(n):
        if len(missing_numbers) < k:
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)
                extra_numbers.add(nums[i])
    # add the remaining missing numbers
    i = 1
    while len(missing_numbers) < k:
        candidate_number = i + n
        # ignore if the array contains the candidate number
        if candidate_number not in extra_numbers:
            missing_numbers.append(candidate_number)
        i += 1
    return missing_numbers


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


if __name__ == "__main__":
    main()


