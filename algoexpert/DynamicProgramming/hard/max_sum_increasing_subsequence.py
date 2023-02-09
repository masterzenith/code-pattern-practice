"""
Max Sum Increasing Subsequence
Write a function that takes in a non-empty array of integers and returns the greatest sum that can be generated from a
strictly-increasing subsequence in the array as well as an array of the numbers in that subsequence.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order
as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do
the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.
You can assume that there will only be one increasing subsequence with the greatest sum.
Sample Input
array = [10, 70, 20, 30, 50, 11, 30]
Sample Output
[110, [10, 20, 30, 50]] // The subsequence [10, 20, 30, 50] is strictly increasing and yields the greatest sum: 110.

Hints:
1. Try building an array of the same length as the input array. At each index in this new array, store the maximum sum
that can be generated from an increasing subsequence ending with the number found at that index in the input array.
2. Can you efficiently keep track of potential sequences in another array? Instead of storing entire sequences, try
storing the indices of previous numbers. For example, at index 3 in this other array, store the index of the before-last
number in the max-sum increasing subsequence ending with the number at index 3.

~~~
This solution uses a bottom-up approach to fill out a dp array dp where dp[i] represents the maximum sum that can be generated
from a strictly-increasing subsequence ending at index i in the input array arr. The loop at line 8 iterates over all indices
j that precede i and updates dp[i] to be the maximum of its current value and the sum of dp[j] + arr[i] if arr[i] > arr[j]
(meaning that arr[j] can be part of a strictly-increasing subsequence ending at arr[i]).
Finally, the loop at lines 14 to 17 iterates over the indices of dp in reverse order and adds the corresponding elements
of arr to the subsequence list whenever dp[i] is equal to the maximum sum in dp. Note that we need to reverse the
subsequence list before returning it because we're building it up in reverse order.
~~~
Optimal Space & Time Complexity
O(n^2) time | O(n) space - where n is the length of the input array.

The time complexity of the solution is O(n^2), where n is the length of the input array arr. This is because the solution
uses two nested loops, the outer loop at line 7 and the inner loop at line 8. The outer loop takes O(n) time and the inner
loop takes O(n) time on average, giving us a total time complexity of O(n^2).
The space complexity of the solution is O(n), where n is the length of the input array arr. This is because the solution
uses an auxiliary array dp of length n to store the maximum sum that can be generated from a strictly-increasing subsequence
ending at each index in arr. In addition, the solution uses a subsequence list to store the numbers in the strictly-increasing
subsequence with the greatest sum, but the space required for this list is proportional to the length of the input array
and hence also O(n).
"""


def greatest_sum_increasing_subsequence(arr):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    max_sum = max(dp)
    subsequence = []
    for i in range(n - 1, -1, -1):
        if max_sum == dp[i]:
            subsequence.append(arr[i])
            max_sum -= arr[i]
    return max(dp), list(reversed(subsequence))


def main():
    array = [10, 70, 20, 30, 50, 11, 30]
    print("Max sum increasing subsequence is: " + str(greatest_sum_increasing_subsequence(array)))


if __name__ == "__main__":
    main()
