"""
Maximize Expression
Write a function that takes in an array of integers and returns the largest possible value for the expression
array[a] - array[b] + array[c] - array[d], where a, b, c, and d are indices of the array and a < b < c < d.
If the input array has fewer than 4 elements, your function should return 0.
Sample Input
array = [3, 6, 1, -3, 2, 7]
Sample Output
4
// Choose a = 1, b = 3, c = 4, and d = 5
// -> 6 - (-3) + 2 - 7 = 4

Hints:
1. The brute-force approach to solving this problem is to simply iterate through every valid choice of a, b, c, and d
and to evaluate the expression at each iteration. While doing this, you can keep track of the maximum value that you
find and return it after considering all possibilities. This solution runs in O(n^4) time; can you think of a way to
solve this faster?
2. You can solve this problem using dynamic programming with a time complexity of O(n); however, you'll need to use
external space.
3. If you know what the maximum possible value of a is at each index in the array, you can find the maximum possible
value of a - b at each individual index in the array in O(1) time (or in O(n) time for all indices). The same thing holds
for finding the maximum possible value of a - b + c if you know the maximum possible value of a - b at each index.
How does this fact help you solve the entire problem in O(n) time?
4. Start by finding the maximum possible value of a at each index in the array, meaning the maximum value of a that you
can obtain at each index i if a is chosen from an index between 0 and i, inclusive. Store all of these values in an array,
and use them to help you determine the maximum possible value of a - b at each index. Do the same for
a - b + c (using the results from a - b) and a - b + c - d (using the results from a - b + c). Once you make it to
a - b + c - d, you'll be able to determine the maximum value of the expression.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the array
The time complexity of the above algorithm is O(n), where n is the number of elements in the input array. This is because
the algorithm makes four passes over the input array to calculate the maximum value of the first three elements,
the maximum value of the second three elements, the minimum value of the third three elements, and the minimum value of
the last three elements. Each pass takes O(n) time, so the overall time complexity is O(n).

The space complexity of the above algorithm is O(1), because it uses only a constant amount of additional memory to store
the intermediate values max_a, max_b, min_c, and min_d, and it does not use any data structures such as arrays or linked
lists to store the input. Thus, the space complexity is constant and equal to O(1).
"""


def maximize_expression(array):
    n = len(array)
    if n < 4:
        return 0
    else:
        max_a = max(array[:n-3])
        max_b = max(array[1:n-2])
        min_c = min(array[2:n-1])
        min_d = min(array[3:])
        return max(max_a - max_b + min_c - min_d, max_a - min_c + max_b - min_d)


def main():
    array = [3, 6, 1, -3, 2, 7]
    print(maximize_expression(array))


if __name__ == "__main__":
    main()
