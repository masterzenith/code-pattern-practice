"""
Spiral Traverse
Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a
one-dimensional array of all the array's elements in spiral order.
Spiral order starts at the top of left corner of the two-dimensional array, goes to the right, and proceeds in a spiral
pattern all the way until every element has been visited.
Sample Input:
array = [
            [1,   2,  3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10,  9,  8, 7],
        ]
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Hints:
1. You can think of the spiral that you have to traverse as a set of rectangle perimeters that progressively get smaller
(i.e., that progressively move inwards in the two-dimensional array).
2. Going off of Hint #1, declare four variables: a starting row, a starting column, an ending row, and an ending column.
These four variables represent the bounds of the first rectangle perimeter in the spiral that you have to traverse.
Traverse that perimeter using those bounds, and then move the bounds inwards. End your algorithm once the starting row
passes the ending row or the starting column passes the ending column.
3. You can solve this problem both iteratively and recursively following very similar logic.
Optimal Space & Time Complexity
O(n) time | O(n) space - where n is the total number of elements in the array
"""


def spiral_traverse(array):
    if len(array) == 0 or len(array[0]) == 0:
        return []
    result = []
    row_up, row_down = 0, len(array) - 1
    col_front, col_back = 0, len(array[0]) - 1
    while row_up <= row_down and col_front <= col_back:
        traverse_boundary(array, row_up, row_down, col_front, col_back, result)
        row_up += 1
        row_down -= 1
        col_front += 1
        col_back -= 1
    return result


def traverse_boundary(array, row_up, row_down, col_front, col_back, result):
    for i in range(col_front, col_back + 1):
        result.append(array[row_up][i])
    for i in range(row_up + 1, row_down + 1):
        result.append(array[i][col_back])
    if row_up != row_down:
        for i in reversed(range(col_front, col_back)):
            result.append(array[row_down][i])
    if col_front != col_back:
        for i in reversed(range(row_up + 1, row_down)):
            result.append(array[i][col_front])


def main():
    array = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]
    print(spiral_traverse(array))


if __name__ == "__main__":
    main()
