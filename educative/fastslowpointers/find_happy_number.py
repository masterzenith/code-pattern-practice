"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the
square of all of its digits, leads us to number 1. All other(no-happy) numbers will never reach 1. Instead, they will
be stuck in a cycle of numbers which does not include 1.
I/P: 23
O/P: true (23 is a happy number)
Explanation: Here are the steps to find out that 23 is a happy number:
1. 2^2 + 3^2 = 4 + 9 = 13
2. 1^2 + 3^2 = 1 + 9 = 10
3. 1^2 + 0 = 1 + 0 = 1

Time: O(logN)
Space: The algorithm runs in constant space O(1).
"""


def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(slow))
        print(fast)
        if slow == fast:  # found the cycle
            break
    return slow == 1  # see if the cycle is stuck on the number 1.


def find_square_sum(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


if __name__ == "__main__":
    main()

