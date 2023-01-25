"""
You are given a set of positive numbers and a target sum 'S'. Each number should be assigned either a '+' or '-' sign.
We need to find the total ways to assign symbols to make the sum of the numbers equal to the target 'S'.
Example 1:
I/P: {1, 1, 2, 3}, S=1
O/P: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}
Example 2:
I/P: {1, 2, 7, 1}, S=9
O/P: 2
Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}

Time: O(N*S)
Space: O(N*S)
"""


def find_target_subsets(num, s):
    total_sum = sum(num)

    # if 's+ total_sum' is odd, we can't find a subset with sum equal to '(s + total_sum) / 2'
    if total_sum < s or  (s + total_sum) % 2 == 1:
        return 0
    # Find the count of subsets of the given numbers whose sum is equal to (S + Sum(num) / 2 )
    return count_subsets(num, (s + total_sum) // 2)


def count_subsets(num, s):
    n = len(num)
    dp = [[0 for x in range(s+1)] for y in range(n)]

    # populate the sum = 0 columns, as we will always have an empty set for zero sum
    for i in range(0, n):
        dp[i][0] = 1

    # with only one number, we can form a subset only when the required sum is equal to the number
    for s in range(1, s + 1):
        dp[0][s] = 1 if num[0] == s else 0

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(1, s+1):
            dp[i][s] = dp[i - 1][s]
            if s >= num[i]:
                dp[i][s] += dp[i-1][s-num[i]]

    # the bottom-right corner will have our answer.
    return dp[n-1][s]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


if __name__ == "__main__":
    main()
