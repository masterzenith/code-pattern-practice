"""
Number Of Ways To Make Change
Given an array of distinct positive integers representing coin denominations and a single non-negative integer n
representing a target amount of money, write a function that returns the number of ways to make change for that target
amount using the given coin denominations.
Note that an unlimited amount of coins is at your disposal.
Sample Input:
n = 6
denoms = [1, 5]

Sample Output:
2 // 1x1 + 1x5 and 6x1

Hints:
1. Try building an array of the number of ways to make change for all amounts between 0 and n inclusive. Note that there
is only one way to make change for 0: that is to not use any coins.
2. Build up the array mentioned in Hint #1 one coin denomination at a time. In other words, find the number of ways to
make change for all amounts between 0 and n with only one denomination, then with two, etc., until you use all
denominations.
https://github.com/lee-hen/Algoexpert/tree/master/medium/14_number_of_ways_to_make_change#hints

Optimal Space & Time Complexity
O(nd) time | O(n) space - where n is the target amount and d is the number of coin denominations
"""


def number_of_ways_to_make_change(n, denoms):
    ways = [0] * (n + 1)
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]


def main():
    n = 6
    denoms = [1, 5]
    print(number_of_ways_to_make_change(n, denoms))


if __name__ == "__main__":
    main()
