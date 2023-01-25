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

Time: O(N*S)
Space: O(N*S)
"""


def count_subsets(num, sum):
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(sum + 1)] for y in range(len(num))]
    return count_subsets_recursive(dp, num, sum, 0)


def count_subsets_recursive(dp, num, sum, current_idx):
    # base checks
    if sum == 0:
        return 1

    n = len(num)
    if n == 0 or current_idx >= n:
        return 0

    # check if we have not already processed a similar problem
    if dp[current_idx][sum] == -1:
        # recursive call after choosing the number at the currentIndex
        # if the number at currentIndex exceeds the sum, we shouldn't process this
        sum1 = 0
        if num[current_idx] <= sum:
            sum1 = count_subsets_recursive(dp, num, sum - num[current_idx], current_idx + 1)
        sum2 = count_subsets_recursive(dp, num, sum, current_idx + 1)
        dp[current_idx][sum] = sum1 + sum2
    return dp[current_idx][sum]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets " + str(count_subsets([1, 2, 7, 1, 5], 9)))


if __name__ == "__main__":
    main()
