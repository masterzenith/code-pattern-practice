"""
River Sizes
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s. Each
0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either
horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size.
Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line;
it can be L-shaped, for example.
Write a function that returns an array of the sizes of all rivers represented in the input matrix. The sizes don't need
to be in any particular order.

Sample Input:
matrix = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
          ]

Sample Output:
[1, 2, 2, 2, 5] // The numbers could be ordered differently.

// The rivers can be clearly seen here:
// [
//   [1,  ,  , 1,  ],
//   [1,  , 1,  ,  ],
//   [ ,  , 1,  , 1],
//   [1,  , 1,  , 1],
//   [1,  , 1, 1,  ],
// ]

Hints:
1. Since you must return the sizes of rivers, which consist of horizontally and vertically adjacent 1s in the input
matrix, you must somehow keep track of groups of neighboring 1s as you traverse the matrix. Try treating the matrix
as a graph, where each element in the matrix is a node in the graph with up to 4 neighboring nodes (above, below, to the
left, and to the right), and traverse it using a popular graph-traversal algorithm like Depth-first Search or
Breadth-first Search.
2. By traversing the matrix using DFS or BFS as mentioned in Hint #1, any time that you encounter a 1 you can traverse
the entire river that this 1 is a part of (and keep track of its size) by simply iterating through the given node's
neighboring nodes and their own neighboring nodes so long as the nodes are 1s.
3. Naturally, many nodes in the graph mentioned in Hint #1 will have overlapping neighboring nodes, and as you traverse
the matrix, you will undoubtedly encounter nodes that you have previously visited. In order to prevent mistakenly
calculating the same river's size multiple times and to avoid doing needless computational work, try keeping track of
every node that you visit in an auxiliary data structure and only performing important computations on unvisited nodes.
What data structure would be ideal here?

Optimal Space & Time Complexity
O(wh) time | O(wh) space - where w and h are the width and height of the input matrix
"""


def river_sizes(matrix):
    # Initialize an empty list to store the sizes of the rivers
    sizes = []
    # Initialize a set to keep track of visited nodes
    visited = set()

    # Define a helper function to traverse the adjacent nodes
    def traverse(i, j, size):
        # If the current node is out of bounds or has already been visited, return
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or (i, j) in visited:
            return 0
        # If the current node is not part of a river, return
        if matrix[i][j] == 0:
            return 0
        # Mark the current node as visited
        visited.add((i, j))
        # Increment the size of the current river
        size += 1
        # Traverse the adjacent nodes in all four directions
        size += traverse(i - 1, j, 0)  # up
        size += traverse(i + 1, j, 0)  # down
        size += traverse(i, j - 1, 0)  # left
        size += traverse(i, j + 1, 0)  # right
        # Return the size of the river
        return size

    # Traverse each node in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # If the current node has not been visited and is part of a river, traverse it and add the size to the list
            # of sizes
            if (i, j) not in visited and matrix[i][j] == 1:
                sizes.append(traverse(i, j, 0))

    # Return the list of river sizes
    return sizes


def main():
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    print(river_sizes(matrix))


if __name__ == "__main__":
    main()
