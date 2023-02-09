"""
Square of Zeroes
Write a function that takes in a square-shaped n x n two-dimensional array of only 1s and 0s and returns a boolean
representing whether the input matrix contains a square whose borders are made up of only 0s.
Note that a 1 x 1 square doesn't count as a valid square for the purpose of this question. In other words, a singular 0
in the input matrix doesn't constitute a square whose borders are made up of only 0s; a square of zeroes has to be at
least 2 x 2.
Sample Input
matrix = [
  [1, 1, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 1],
  [0, 1, 1, 1, 0, 1],
  [0, 0, 0, 1, 0, 1],
  [0, 1, 1, 1, 0, 1],
  [0, 0, 0, 0, 0, 1],
]
Sample Output
true
[
  [ ,  ,  ,  ,  ,  ],
  [0, 0, 0, 0, 0,  ],
  [0,  ,  ,  , 0,  ],
  [0,  ,  ,  , 0,  ],
  [0,  ,  ,  , 0,  ],
  [0, 0, 0, 0, 0,  ],
]

Hints:
1. For the purpose of this question, a square is defined by its topmost and bottommost rows and by its leftmost and
rightmost columns. Given a pair of rows and a pair of columns that form a valid square, you can easily determine if the
relevant square is a square of zeroes with two for loops.
2. You can apply the logic described in Hint #1 on every valid square in the input matrix in order to solve this problem.
To find every valid square, you can either traverse the matrix iteratively with three nested loops, or you can start out
at the outtermost square and recursively go inwards in the matrix, checking the squares obtained by moving each corner of
a square inwards. If you go with this recursive approach, you'll need to use a cache to avoid doing many duplicate computations.
3. The operation described in Hint #1 is a computationally expensive one to have to repeat for every single square in the
matrix. Can you precompute certain values to make this operation a constant-time operation?
4. You can make the operation described in Hint #1 a constant-time operation by precomputing some values in the matrix.
Specifically, you can precompute two values for every element in the matrix: the number of 0s to the right of each element
(including the element itself) and the number of 0s below each element (including the element itself). You can compute
these values by iterating through the matrix starting at the bottom of the right corner and moving your way up by traversing
each row from right to left; applying some simple dynamic programming techniques will allow you to build up these values
trivially. Once you have these values precomputed, you can perform the operation described in Hint #1 in constant time
just by looking at the number of 0s below any square's two top corners and the number of 0s to the right of the same
square's two left corners.

Optimal Space & Time Complexity
O(n^3) time | O(n^2) space - where n is the height and width of the matrix

Hints:
https://github.com/lee-hen/Algoexpert/tree/master/very_hard/16_square_of_zeroes#hints
"""


def square_of_zeroes(matrix):
    info_matrix = pre_compute_num_of_zeroes(matrix)
    n = len(matrix)
    for top_row in range(n):
        for left_col in range(n):
            square_length = 2
            while square_length <= n - left_col and square_length <= n - top_row:
                bottom_row = top_row + square_length - 1
                right_col = left_col + square_length - 1
                if is_square_of_zeroes(info_matrix, top_row, left_col, bottom_row, right_col):
                    return True
                square_length += 1
    return False


def is_square_of_zeroes(info_matrix, r1, c1, r2, c2):
    square_length = c2 - c1 + 1
    has_top_border = info_matrix[r1][c1]["num_zeroes_right"] >= square_length
    has_left_border = info_matrix[r1][c1]["num_zeroes_below"] >= square_length
    has_bottom_border = info_matrix[r2][c1]["num_zeroes_right"] >= square_length
    has_right_border = info_matrix[r1][c2]["num_zeroes_below"] >= square_length
    return has_top_border and has_left_border and has_bottom_border and has_right_border


def pre_compute_num_of_zeroes(matrix):
    info_matrix = [[x for x in row] for row in matrix]
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            num_zeroes = 1 if matrix[row][col] == 0 else 0
            info_matrix[row][col] = {
                "num_zeroes_below": num_zeroes,
                "num_zeroes_right": num_zeroes,
            }
    last_idx = len(matrix) - 1
    for row in reversed(range(n)):
        for col in reversed(range(n)):
            if matrix[row][col] == 1:
                continue
            if row < last_idx:
                info_matrix[row][col]["num_zeroes_below"] += info_matrix[row+1][col]["num_zeroes_below"]
            if col < last_idx:
                info_matrix[row][col]["num_zeroes_right"] += info_matrix[row][col+1]["num_zeroes_right"]
    return info_matrix


def main():
    matrix = [
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1],
    ]
    print(square_of_zeroes(matrix))


if __name__ == "__main__":
    main()
