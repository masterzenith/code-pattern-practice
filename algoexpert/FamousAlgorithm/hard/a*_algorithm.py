"""
A* Algorithm
You're given a two-dimensional array containing 0s and 1s, where each 0 represents a free space and each 1 represents an
obstacle (a space that cannot be passed through). You can think of this array as a grid-shaped graph. You're also given
four integers startRow, startCol, endRow, and endCol, representing the positions of a start node and an end node in the graph.
Write a function that finds the shortest path between the start node and the end node using the A* search algorithm and returns it.
The shortest path should be returned as an array of node positions, where each node position is an array of two elements:
the [row, col] of the respective node in the graph. The output array should contain the start node's position, the end
node's position, and all the positions of the remaining nodes in the shortest path, and these node positions should
be ordered from start node to end node.
If there is no path from the start node to the end node, your function should return an empty array.
Note that:
- From each node in the graph, you can only travel in four directions: up, left, down and right; you can't travel diagonally.
- The distance between all neighboring nodes in the graph is the same; you can treat it as a distance of 1.
- The start node and end node are guaranteed to be located in empty spaces (cells containing 0).
- The start node and end node will never be out of bounds and will never overlap.
- There will be at most one shortest path from the start node to the end node.
If you're unfamiliar with A*, we recommend watching the Conceptual Overview section of this question's video explanation
before starting to code.

Sample Input:
startRow = 0
startCol = 1
endRow = 4
endCol = 3
graph = [
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 1, 1],
  [0, 0, 0, 0, 0],
]

Sample Output:
[[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]

// The shortest path can be clearly seen here:
// [
//   [., ., 0, 0, 0],
//   [., 1, 1, 1, 0],
//   [., ., 0, 0, 0],
//   [1, ., 1, 1, 1],
//   [0, ., ., ., 0],
// ]

Hints:
1. A* works by visiting nodes in the graph, one by one, all the while keeping track of their shortest estimated distance
to the end node and continuously updating these distances. More specifically, the algorithm keeps track of unvisited nodes
and visits the unvisited node with the shortest estimated distance to the end node at any point in time, naturally starting
with the start node. Whenever the algorithm visits an unvisited node, it looks at all of its neighboring nodes and tries
to update their shortest estimated distance to the end node, using the current shortest distance to the current node as
a base and using a special heuristic to estimate the remaining distance to the end node. In a grid-shaped graph, the
heuristic used is often the Manhattan Distance (i.e., the number of naive vertical and horizontal steps between the current
node and the end node). Once the algorithm has reached the end node, it is guaranteed to have found the shortest path to it.
How can you implement this algorithm?
2. The most challenging part of A* is determining how to efficiently find the node with the current shortest estimated
distance to the end. Can you think of a data structure that could be used to keep track of the distances and to efficiently
retrieve the node with the current shortest estimated distance to the end at each step?
3. Create a min-heap that will hold all of the unvisited nodes and their current shortest estimated distance to the end
node. Initialize all nodes except for the start node as having a shortest estimated distance to the end node of infinity
and also a shortest distance from the start node to themselves of infinity; the start node will have a distance to itself
of 0 and an estimated distance to the end node of its Manhattan Distance to the end node. Next, write a while loop that
will run until the min-heap is empty or until the end node is reached. At every iteration in the loop, remove the node
from the top of the heap (the node with the shortest estimated distance to the end node), loop through all of its neighboring
nodes, and for each neighbor, update its two distances if reaching the neighbor from the current node yields a shorter
distance than whatever's already stored on the neighbor. Once you reach the end node, you'll have found the shortest path
to it from the start node. Note that you'll have to keep track of which node each node came from whenever you update node
distances; this is so that you can reconstruct the shortest path once you reach the end node.

Optimal Space & Time Complexity
O(w * h * log(w * h)) time | O(w * h) space - where w is the width of the graph and h is the height

https://github.com/lee-hen/Algoexpert/tree/master/very_hard/18_a_star_algorithm#hints
https://github.com/das-jishu/algoexpert-data-structures-algorithms/blob/master/Very%20Hard/A-star-algorithm.py
"""


class Node:
    def __init__(self, row, col, value):
        self.id = str(row) + "-" + str(col)
        self.row = row
        self.col = col
        self.value = value
        self.distance_from_start = float("inf")
        self.estimated_distance_to_end = float("inf")
        self.came_from = None


class MinHeap:
    def __init__(self, array):
        self.node_positions_in_heap = {node.id: idx for idx, node in enumerate(array)}
        self.heap = self.build_heap(array)

    def is_empty(self):
        return len(self.heap) == 0

    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array

    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and \
                    heap[child_two_idx].estimated_distance_to_end < heap[child_one_idx].estimated_distance_to_end:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if heap[idx_to_swap].estimated_distance_to_end < heap[current_idx].estimated_distance_to_end:
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return

    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and \
                heap[current_idx].estimated_distance_to_end < heap[parent_idx].estimated_distance_to_end:
            self.swap(current_idx, parent_idx, heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def swap(self, i, j, heap):
        self.node_positions_in_heap[heap[i].id] = j
        self.node_positions_in_heap[heap[j].id] = i
        heap[i], heap[j] = heap[j], heap[i]

    # O(log(n)) time and O(1) space
    def remove(self):
        if self.is_empty():
            return

        self.swap(0, len(self.heap) - 1, self.heap)
        node = self.heap.pop()
        del self.node_positions_in_heap[node.id]
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return node

    def insert(self, node):
        self.heap.append(node)
        self.node_positions_in_heap[node.id] = len(self.heap) - 1
        self.sift_up(len(self.heap) - 1, self.heap)

    def contains_node(self, node):
        return node.id in self.node_positions_in_heap

    def update(self, node):
        self.sift_up(self.node_positions_in_heap[node.id], self.heap)


def a_star_algorithm(start_row, start_col, end_row, end_col, graph):
    nodes = initialize_nodes(graph)
    start_node = nodes[start_row][start_col]
    end_node = nodes[end_row][end_col]

    start_node.distance_from_start = 0
    start_node.estimated_distance_to_end = calculate_manhattan_distance(start_node, end_node)

    nodes_to_visit = MinHeap([start_node])

    while not nodes_to_visit.is_empty():
        current_min_distance_node = nodes_to_visit.remove()
        if current_min_distance_node == end_node:
            break

        neighbors = get_neighboring_nodes(current_min_distance_node, nodes)
        for neighbor in neighbors:
            if neighbor.value == 1:
                continue
            tentative_distance_to_neighbor = current_min_distance_node.distance_from_start + 1
            if tentative_distance_to_neighbor >= neighbor.distance_from_start:
                continue
            neighbor.came_from = current_min_distance_node
            neighbor.distance_from_start = tentative_distance_to_neighbor
            neighbor.estimated_distance_to_end = tentative_distance_to_neighbor + \
                                                 calculate_manhattan_distance(neighbor, end_node)
            if not nodes_to_visit.contains_node(neighbor):
                nodes_to_visit.insert(neighbor)
            else:
                nodes_to_visit.update(neighbor)
    return reconstruct_path(end_node)


def initialize_nodes(graph):
    nodes = []
    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))
    return nodes


def calculate_manhattan_distance(current_node, end_node):
    current_row = current_node.row
    current_col = current_node.col
    end_row = end_node.row
    end_col = end_node.col

    return abs(current_row - end_row) + abs(current_col - end_col)


def get_neighboring_nodes(node, nodes):
    neighbors = []
    num_rows = len(nodes)
    num_cols = len(nodes[0])

    row = node.row
    col = node.col

    if row < num_rows - 1:
        neighbors.append(nodes[row+1][col])

    if row > 0:
        neighbors.append(nodes[row-1][col])

    if col < num_cols - 1:
        neighbors.append(nodes[row][col+1])

    if col > 0:
        neighbors.append(nodes[row][col-1])
    return neighbors


def reconstruct_path(end_node):
    if not end_node.came_from:
        return []

    current_node = end_node
    path = []

    while current_node is not None:
        path.append([current_node.row, current_node.col])
        current_node = current_node.came_from
    return path[::-1]


def main():
    startRow = 0
    startCol = 1
    endRow = 4
    endCol = 3
    graph = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    print(a_star_algorithm(startRow, startCol, endRow, endCol, graph))


if __name__ == "__main__":
    main()


