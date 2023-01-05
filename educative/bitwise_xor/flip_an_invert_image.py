"""
Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.
To flip an image horizontally means that each row of the image is reversed. For example, flipping [0, 1, 1]
horizontally results in [1, 1, 0].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [1, 1, 0]
results in [0, 0, 1].

I/P: [
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
]

O/P: [
    [0, 1, 0],
    [0, 0, 0],
    [0, 0, 1]
]
Explanation: First reverse each row: [[1, 0, 1], [1, 1, 1], [1, 1, 0]].
            Then invert the image: [[0, 1, 0], [0, 0, 0], [0, 0, 1]]

Time: O(n) as we iterate through all elements of the input
Space: The space complexity of this solution is O(1)
"""


def find_an_invert_image(matrix):
    c = len(matrix)
    for row in matrix:
        for i in range((c + 1) // 2):
            row[i], row[c - i - 1] = row[c - i - 1] ^ 1, row[i] ^ 1
    return matrix


def main():
    print(find_an_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(find_an_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


if __name__ == "__main__":
    main()
