"""
Maximum Sum Submatrix
You're given a two-dimensional array (a matrix) of potentially unequal height and width that's filled with integers.
You're also given a positive integer size. Write a function that returns the maximum sum that can be generated from a
submatrix with dimensions size * size.
For example, consider the following matrix:
[
  [2, 4],
  [5, 6],
  [-3, 2],
]
If size = 2, then the 2x2 submatrices to consider are:
[2, 4]
[5, 6]
------
[5, 6]
[-3, 2]
The sum of the elements in the first submatrix is 17, and the sum of the elements in the second submatrix is 10. In this
example, your function should return 17.
Note: size will always be at least 1, and the dimensions of the input matrix will always be at least size * size.
Sample Input:
matrix =
[
  [5, 3, -1, 5],
  [-7, 3, 7, 4],
  [12, 8, 0, 0],
  [1, -8, -8, 2],
]
size = 2
Sample Output:
18
// [
//   [., ., ., .],
//   [., 3, 7, .],
//   [., 8, 0, .],
//   [., ., ., .],
// ]

Hints:
1. The brute-force approach to solve this problem involves simply considering all possible submatrices of size
size * size, determining their sums, and finally returning the maximum sum. This approach is acceptable, but it isn't
optimal. Why isn't it optimal?
2. The approach stated in Hint #1 isn't optimal because it repeats some additions. When considering submatrices of any
size larger than 1, it's almost always the case that some these matrices will have overlapping elements, meaning that
we'll repeatedly add up the same numbers. If we were to use the brute-force approach, we would get a time complexity of
O(width * height * size). To achieve a more optimal time complexity, we need to avoid readding elements that have already
been added. Can you think of a way to solve this problem in O(width * height) time?
3. To avoid doing repeated addition, we have to use auxiliary space. Ideally, this extra space will allow us to determine
the sum of a submatrix of any size in constant time. Start by creating a matrix with the same dimensions as the input
matrix (we call this matrix sums). The element at position i, j (where i is the row and j is the column) in this new matrix
should be the sum of all the elements in the submatrix whose top left corner is at 0, 0 and whose bottom right corner is
at i, j. How can you quickly fill up this new matrix, and how can you then use it to determine the sum of a submatrix of
any size in constant time?
4. The sum of a matrix whose bottom right corner is at i, j (where size <= i <= j) is simply
sums[i][j] - sums[i - size][j] - sums[i][j - size] + sums[i - size][j - size]. See the Conceptual Overview section of
this question's video explanation for a more in-depth explanation.

Optimal Space & Time Complexity
O(w * h) time | O(w * h) space - where w is the width of the matrix and h is the height

Image Explanation:
https://github.com/lee-hen/Algoexpert/tree/master/hard/19_maximum_sum_submatrix#hints
"""


def maximum_sum_submatrix(matrix, size):
    sums = create_sum_matrix(matrix)
    max_sum = float("-inf")
    for row in range(size - 1, len(matrix)):
        for col in range(size - 1, len(matrix[row])):
            total = sums[row][col]
            touches_top_border = row - size < 0
            if not touches_top_border:
                total -= sums[row - size][col]
            touches_left_border = col - size < 0
            if not touches_left_border:
                total -= sums[row][col - size]
            if not touches_top_border and not touches_left_border:
                total += sums[row - size][col - size]
            max_sum = max(max_sum, total)
    return max_sum


def create_sum_matrix(matrix):
    sums = [[0 for _ in range(len(matrix[row]))] for row in range(len(matrix))]
    sums[0][0] = matrix[0][0]
    for idx in range(1, len(matrix[0])):
        sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]
    for idx in range(1, len(matrix)):
        sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            sums[row][col] = sums[row - 1][col] + sums[row][col - 1] - sums[row - 1][col - 1] + matrix[row][col]
    return sums


def main():
    matrix = [
        [5, 3, -1, 5],
        [-7, 3, 7, 4],
        [12, 8, 0, 0],
        [1, -8, -8, 2],
    ]
    size = 2
    print(maximum_sum_submatrix(matrix, size))


if __name__ == "__main__":
    main()
