"""
Zigzag Traverse:
Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a
one-dimensional array of all the array's elements in zigzag order.
Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element, and proceeds in a
zigzag pattern all the way to the bottom right corner.

Sample Input:
array = [
    [1,  3,  4, 10],
    [2,  5,  9, 11],
    [6,  8, 12, 15],
    [7, 13, 14, 16],
]
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Hints:
1. Don't overthink this question by trying to come up with a clever way of getting the zigzag order. Think about the
simplest checks that need to be made to decide when and how to change direction throughout the zigzag traversal.
2. Starting at the top of left corner, iterate through the two-dimensional array by keeping track of the direction that
you're moving in (up or down). If you're moving up, you know that you need to move in an up-right pattern and that you
need to handle the case where you hit the top or the right borders of the array. If you're moving down, you know that
you need to move in a down-left pattern and that you need to handle the case where you hit the left or the bottom
borders of the array.
3. When going up, if you hit the right border, you'll have to go down one element; if you hit the top border, you'll
have to go right one element. Similarly, when going down, if you hit the left border, you'll have to go down one element;
if you hit the bottom border, you'll have to go right one element.

Optimal Space & Time Complexity
O(n) time | O(n) space - where n is the total number of elements in the two-dimensional array
"""


def zigzag_traverse(array):
    total_rows, total_cols = len(array), len(array[0])
    zigzag_traverse = []
    row, col = 0, 0
    direction = 'down'
    while row in range(total_rows) and col in range(total_cols):
        while row in range(total_rows) and col in range(total_cols):
            zigzag_traverse.append(array[row][col])
            print("currently in ", row, col)
            row = row - 1 if direction == 'up' else row + 1
            col = col + 1 if direction == 'up' else col - 1
        if direction == 'up':
            if col < total_cols:
                row = 0
            else:
                col = total_cols - 1
                row += 2
        else:
            if row < total_rows:
                col = 0
            else:
                row = total_rows - 1
                col += 2
        next_start = (row, col)
        print(next_start)
        direction = 'down' if direction == 'up' else 'up'
    return zigzag_traverse


def main():
    array = [
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16],
    ]
    print(zigzag_traverse(array))


if __name__ == "__main__":
    main()
