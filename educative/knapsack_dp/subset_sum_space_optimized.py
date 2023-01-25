"""
Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number 'S'.
Example 1:
I/P: {1, 2, 3, 7}, S=6
O/P: True
The given set has a subset whose sum is '6': {1, 2, 3}

Example 2:
I/P: {1, 2, 7, 1, 5}, S=10
O/P: True
The given set has a subset whose sum is '10': {1, 2, 7}

Example 3:
I/P: {1, 3, 4, 8}, S=6
O/P: False
The given set does not have any subset whose sum is equal to '6'.

Time: O(N*S) where 'N' represents total numbers and 'S' is the required sum.
Space: O(S) where 'S' is the required sum. Single array solution.
"""


def can_partition(num, sum):
    n = len(num)
    dp = [False for x in range(sum+1)]

    # handle sum=0, as we can always have '0' sum with an empty set
    dp[0] = True

    # with only one number, we can form a subset only when the required sum is equal to its value
    for s in range(1, sum + 1):
        dp[s] = num[0] == s

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(sum, -1, -1):
            # if dp[s] == true, this means we can get the sum 's' without num[i], hence we can move on to the next
            # number else we can include num[i] and see if we can find a subset to get the remaining sum
            if not dp[s] and s >=num[i]:
                dp[s] = dp[s - num[i]]
    return dp[sum]


def main():
    print("Can Partition: " +
          str(can_partition([1, 2, 3, 7], 6)))
    print("Can Partition: " +
          str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can Partition: " +
          str(can_partition([1, 3, 4, 8], 6)))


if __name__ == "__main__":
    main()
