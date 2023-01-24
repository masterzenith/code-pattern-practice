"""
We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'. The array originally contained all
the numbers from 1 to 'n', but due to a data error, one of the numbers got duplicated which also resulted in one number
going missing. Find both these numbers.
Example 1:
I/P: [3, 1, 2, 5, 2]
O/P: [2, 4]
Explanation: '2' is duplicated and '4' is missing.

Example 2:
I/P: [3, 1, 2, 3, 6, 4]
O/P: [3, 5]
Explanation: '3' is duplicated and '5' is missing.

Time: The time complexity of the above algorithm is O(n)
Space: The algorithm runs in constant space O(1)
"""


def find_corrupt_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]
    return [-1, -1]


def main():
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


if __name__ == "__main__":
    main()
