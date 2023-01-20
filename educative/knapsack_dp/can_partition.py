"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both
subsets is equal.

Example 1:
Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

Example 2:
Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}

Solution1: Top-down DP with Memoization

Time & Space: The above algorithm has the time and space complexity of O(N*S), where 'N' represents total numbers and
            'S' is the total sum of all the numbers.
"""


def can_partition(num):
    s = sum(num)

    # if 's' is an add number, we can't have two subsets with equal sum
    if s % 2 != 0:
        return False

    # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
    dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(num))]
    return True if can_partition_recursive(dp, num, int(s / 2), 0) == 1 else False


def can_partition_recursive(dp, num, sum, current_idx):
    # base case
    if sum == 0:
        return 1

    n = len(num)
    if n == 0 or current_idx >= n:
        return 0

    # if we have not already processed a similar problem
    if dp[current_idx][sum] == -1:
        # recursive call after choosing the number at the current_idx
        # if the number at current_idx exceeds the sum, we shouldn't process this
        if num[current_idx] <= sum:
            if can_partition_recursive(dp, num, sum - num[current_idx], current_idx + 1) == 1:
                dp[current_idx][sum] = 1
                return 1

            # recursive call after excluding the number at the current_idx
            dp[current_idx][sum] = can_partition_recursive(dp, num, sum, current_idx + 1)
    return dp[current_idx][sum]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


if __name__ == "__main__":
    main()