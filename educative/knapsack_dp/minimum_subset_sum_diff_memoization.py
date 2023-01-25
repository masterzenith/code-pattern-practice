"""
Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.
Example 1:
I/P: {1, 2, 3, 9}
O/P: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference between the sum of
numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}

Example 2:
I/P: {1, 2, 7, 1, 5}
O/P: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference between the sum of number
is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}

Example 3:
I/P: {1, 3, 100, 4}
O/P: 92
Explanation: We can partition the given set into two subsets where minimum absolute difference between the sum of
numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.

Time: O(N*S)
Space: O(N*S)
"""


def can_partition(num):
    s = sum(num)
    dp = [[-1 for x in range(s+1)] for y in range(len(num))]
    return can_partition_recursive(dp, num, 0, 0, 0)


def can_partition_recursive(dp, num, current_idx, sum1, sum2):
    # base check
    if current_idx == len(num):
        return abs(sum1 - sum2)

    # check if we have not already processed similar problem
    if dp[current_idx][sum1] == -1:
        # recursive call after including the number at the current Index in the first set
        diff1 = can_partition_recursive(dp, num, current_idx + 1, sum1 + num[current_idx], sum2)

        # recursive call after including the number at the current Index in the second set
        diff2 = can_partition_recursive(dp, num, current_idx + 1, sum1 , sum2 + num[current_idx])
        dp[current_idx][sum1] = min(diff1, diff2)

    return dp[current_idx][sum1]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


if __name__ == "__main__":
    main()
