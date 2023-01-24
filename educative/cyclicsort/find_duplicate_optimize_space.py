"""
We are given an unsorted array containing 'n+1' numbers taken from the range 1 to 'n'. The array has only one duplicate
but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however,
allowed to modify the input array.
Can we solve the above problem in O(1) space and without modifying the input array?
Example 1:
I/P: [1, 4, 4, 3, 2]
O/P: 4

Example 2:
I/P: [2, 1, 3, 3, 5, 4]
O/P: 3

Example 3:
I/P: [2, 4, 1, 4, 4]
O/P: 4

Time: The time complexity of the above algorithm is O(n).
Space: The algorithm runs in constant space O(1).
"""


def find_duplicate(nums):
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    # find cycle length
    current = nums[nums[slow]]
    cycle_length = 1
    while current != nums[slow]:
        current = nums[current]
        cycle_length += 1
    return find_start(nums, cycle_length)


def find_start(nums, cycle_length):
    pointer1, pointer2 = nums[0], nums[0]
    # move pointer2 ahead 'cycle_length' steps
    while cycle_length > 0:
        pointer2 = nums[pointer2]
        cycle_length -= 1

    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = nums[pointer1]
        pointer2 = nums[pointer2]
    return pointer1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


if __name__ == "__main__":
    main()
