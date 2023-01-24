"""
We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'. The array has some numbers
appearing twice, find all these duplicate numbers without using any extra space.
Example 1:
I/P: [3, 4, 4, 5, 5]
O/P: [4, 5]

Example 2:
I/P: [5, 4, 7, 2, 3, 5, 3]
O/P: [3, 5]

Time: The time complexity of the above algorithm is O(n).
Space: Ignoring the space required for storing the duplicates, the algorithm runs in constant space O(1).
"""


def find_all_duplicates(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    duplicate_numbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate_numbers.append(nums[i])
    return duplicate_numbers


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


if __name__ == "__main__":
    main()
