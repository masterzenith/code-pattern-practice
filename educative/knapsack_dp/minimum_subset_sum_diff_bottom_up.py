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

Time: O(N*S), where 'N' represents total numbers and 'S' is the total sum of all the numbers.
Space: O(S)
"""


def can_partition(num):
    s = sum(num)
    n = len(num)
    dp = [[False for x in range(int(s/2)+1)] for y in range(n)]

    # populate the s=0 columns, as we can always from '0' sum with an empty set
    for i in range(0, n):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is equal to that number
    for j in range(0, int(s/2) + 1):
        dp[0][j] = num[0] == j

    # Process all subsets for all sums
    for i in range(1, n):
        for j in range(1, int(s/2) + 1):
            # If we can get the sum 's' without the number at index 'i'
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                # else include the number and see if we can find a subset to get the remaining sum
                dp[i][j] = dp[i-1][j-num[i]]
    sum1 = 0
    # find the largest index in the last row which is true
    for i in range(int(s/2), -1, -1):
        if dp[n-1][i]:
            sum1 = i
            break
    sum2 = s - sum1
    return abs(sum2 - sum1)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


if __name__ == "__main__":
    main()
