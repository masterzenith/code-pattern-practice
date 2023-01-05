"""
In a non-empty array of integers, every number appears twice except for one, find that single number.
I/P: 1, 4, 2, 1, 3, 2, 3
O/P: 4

I/P: 7, 9, 7
O/P: 9

Two properties of XOR:
    - It returns zero if we take XOR of two same numbers
    - It returns the same number if we XOR with zero
So we can XOR all the numbers in the input; duplicate numbers will zero out each other and we will be left with the
single number.

Time: O(n) as we iterate through all numbers of the input once.
Space: The algorithm runs in constant space O(1).
"""


def find_single_number(arr):
    num = 0
    for i in arr:
        num ^= i
    return num


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))


if __name__ == "__main__":
    main()