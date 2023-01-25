"""
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number 'S'.
Example 1:
I/P: {1, 1, 2, 3}, S= 4
O/P: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}

Example 2:
I/P: {1, 2, 7, 1, 5}, S=9
O/P: 3
The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

Time: O(N*S), where N is the total numbers and S is the desired sum.
Space: O(S)
"""


def count_subsets(num, sum):
    n = len(num)
    dp = [0 for x in range(sum + 1)]
    dp[0] = 1

    # with only one number, we can form a subset only when the required sum is equal to its value
    for s in range(1, sum + 1):
        dp[s] = 1 if num[0] == s else 0

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(sum, -1, -1):
            # include the number, if it does not exceed the sum
            if s >= num[i]:
                dp[s] += dp[s - num[i]]
    # The bottom-right corner will have our answer
    return dp[sum]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets " + str(count_subsets([1, 2, 7, 1, 5], 9)))


if __name__ == "__main__":
    main()
