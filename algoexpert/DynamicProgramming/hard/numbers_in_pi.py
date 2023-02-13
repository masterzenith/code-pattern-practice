"""
Numbers In Pi
Given a string representation of the first n digits of Pi and a list of positive integers (all in string format), write
a function that returns the smallest number of spaces that can be added to the n digits of Pi such that all resulting
numbers are found in the list of integers.
Note that a single number can appear multiple times in the resulting numbers. For example, if Pi is "3141" and the numbers
are ["1", "3", "4"], the number "1" is allowed to appear twice in the list of resulting numbers after three spaces are
added: "3 | 1 | 4 | 1".
If no number of spaces to be added exists such that all resulting numbers are found in the list of integers, the function
should return -1.

Sample Input
pi = "3141592653589793238462643383279",
numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]

Sample Output
2 // "314159265 | 35897932384626433832 | 79"

Hints:
1. You'll need to look numbers up quickly; is the input array the best data structure for this?
2. Dump every favorite number in a hash table for fast look-up. Iterate through the digits of Pi, checking if every
prefix of the n digits is a favorite number. What should you do if you find that a prefix of the n digits of Pi is a
favorite number?
3. Going off of Hint #2, if you find a prefix of the n digits of Pi that is a favorite number, try adding 1 space after
it and then recursively calculating the smallest number of spaces in the suffix that comes after it. Do this for every
prefix, and you'll find the answer. Can this method be optimized with a cache?

Optimal Space & Time Complexity
O(n^3 + m) time | O(n + m) space - where n is the number of digits in Pi and m is the number of favorite numbers

https://github.com/das-jishu/algoexpert-data-structures-algorithms/blob/master/Hard/numbers-pi.py
"""


def numbers_in_pi(pi, numbers):
    number = {}
    for num in numbers:
        number[num] = True
    return find_min_spaces(pi, 0, number, 0)


def find_min_spaces(pi, index, number, space_count):
    if index >= len(pi):
        print(space_count)
        return space_count - 1
    min_spaces = float('inf')
    for i in range(index, len(pi)):
        if pi[index: i+1] in number:
            spaces = find_min_spaces(pi, i+1, number, space_count + 1)
            if spaces != -1:
                min_spaces = min(min_spaces, spaces)
    return -1 if min_spaces == float('inf') else min_spaces


def main():
    pi = "3141592653589793238462643383279",
    numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
    print(numbers_in_pi(pi, numbers))


if __name__ == "__main__":
    main()
