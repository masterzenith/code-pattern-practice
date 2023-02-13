"""
Dijkstra's Algorithm
You're given an integer start and a list edges of pairs of integers.
The list is what's called an adjacency list, and it represents a graph. The number of vertices in the graph is equal to
the length of edges, where each index i in edges contains vertex i's outbound edges, in no particular order. Each individual
edge is represented by an pair of two numbers, [destination, distance], where the destination is a positive integer denoting
the destination vertex and the distance is a positive integer representing the length of the edge (the distance from vertex i
to vertex destination). Note that these edges are directed, meaning that you can only travel from a particular vertex to its
destination—not the other way around (unless the destination vertex itself has an outbound edge to the original vertex).

Write a function that computes the lengths of the shortest paths between start and all the other vertices in the graph
using Dijkstra's algorithm and returns them in an array. Each index i in the output array should represent the length of
shortest path between start and vertex i. If no path is found from start to vertex i, then output[i] should be -1.
Note that the graph represented by edges won't contain any self-loops (vertices that have an outbound edge to themselves)
and will only have positively weighted edges (i.e., no negative distances).
If you're unfamiliar with Dijkstra's algorithm, we recommend watching the Conceptual Overview section of this question's
video explanation before starting to code.

Sample Input:
start = 0
edges = [
  [[1, 7]],
  [[2, 6], [3, 20], [4, 3]],
  [[3, 14]],
  [[4, 2]],
  [],
  [],
]
Sample Output:
[0, 7, 13, 27, 10, -1]

Hints:
1. Dijkstra's algorithm works by visiting vertices in the graph, one by one, all the while keeping track of the current
shortest distances from the start vertex to all other vertices and continuously updating these shortest distances. More
specifically, the algorithm keeps track of unvisited vertices and visits the unvisited vertex with the shortest distance
at any point in time, naturally starting with the start vertex. Whenever the algorithm visits an unvisited vertex, it
looks at all of its outbound edges and tries to update the shortest distances from the start to the destinations in the
edges, using the current shortest distance to the current vertex as a base. Once the algorithm has visited all the
vertices and considered all of their edges, it is guaranteed to have found the shortest path to each vertex. How can you
implement this algorithm?
2. The most challenging part of Dijkstra's algorithm is determining how to efficiently find the vertex with the current
shortest distance. Can you think of a data structure that could be used to keep track of the distances and to efficiently
retrieve the vertex with the current shortest distance at each step?
3. Create an array that can store the final shortest distances between the start vertex and all other vertices, as well
as a min-heap that will hold all the unvisited vertices and their current shortest distances. For both the final
distances array and the min-heap, initialize all vertices except for the start node as having a distance of infinity; the
start node will have a distance 0. Next, write a while loop that will run until the min-heap is empty. At every iteration
in the loop, remove the vertex from the top of the heap (the vertex with the shortest distance), loop through all of its
edges, and for each edge, update the shortest distance of the destination vertex to be the minimum of the destination's
current shortest distance and the currently visited vertex's distance plus the current edge's weight. Once the heap is empty,
all the vertices will have been visited, and you'll have the shortest distances to all vertices stored in your distances
array.

Optimal Space & Time Complexity
O((v + e) * log(v)) time | O(v) space - where v is the number of vertices and e is the number of edges in the input graph

https://github.com/lee-hen/Algoexpert/tree/master/hard/17_dijkstras_algorithm#hints
https://github.com/das-jishu/algoexpert-data-structures-algorithms/blob/master/Hard/dijkstra-algorithm.py
"""


class MinHeap:
    def __init__(self, array):
        self.vertex_map = {idx: idx for idx in range(len(array))}
        self.heap = self.build_heap(array)

    def is_empty(self):
        return len(self.heap) == 0

    # O(N) time and O(1) space
    def build_heap(self, array):
        first_parent = (len(array) - 2) // 2
        for current_idx in reversed(range(first_parent + 1)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array

    # O(logN) time and O(1) space
    def sift_down(self, start, end_idx, heap):
        child_one_idx = start * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = start * 2 + 2 if start * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx][1] < heap[child_one_idx][1]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if heap[idx_to_swap][1] < heap[start][1]:
                self.swap(start, idx_to_swap, heap)
                start = idx_to_swap
                child_one_idx = start * 2 + 1
            else:
                return

    # O(logN) time and O(1) space
    def sift_up(self, start, heap):
        parent_idx = (start - 1) // 2
        while start > 0 and heap[start][1] < heap[parent_idx][1]:
            self.swap(start, parent_idx, heap)
            start = parent_idx
            parent_idx = (start - 1) // 2

    def swap(self, i, j, array):
        self.vertex_map[array[i][0]] = j
        self.vertex_map[array[j][0]] = i
        array[i], array[j] = array[j], array[i]

    # O(log(n)) time and O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        vertex, distance = self.heap.pop()
        self.vertex_map.pop(vertex)
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return vertex, distance

    def update(self, vertex, value):
        self.heap[self.vertex_map[vertex]] = (vertex, value)
        self.sift_up(self.vertex_map[vertex], self.heap)


# O((V+E)* log(V)) time and O(V) space, E -> Total number of edges
def dijkstras_algorithm(start, edges):
    distances = [float('inf')] * len(edges)
    distances[start] = 0
    min_distance_heap = MinHeap([(idx, float('inf')) for idx in range(len(edges))])
    min_distance_heap.update(start, 0)

    while not min_distance_heap.is_empty():
        next_vertex, min_distance = min_distance_heap.remove()
        if min_distance == float('inf'):
            break

        for pair in edges[next_vertex]:
            destination = pair[0]
            distance = pair[1]
            path_length = distances[next_vertex] + distance
            if path_length < distances[destination]:
                distances[destination] = path_length
                min_distance_heap.update(destination, path_length)

    for i, distance in enumerate(distances):
        if distance == float('inf'):
            distances[i] = -1
    return distances


def main():
    start = 0
    edges = [
        [[1, 7]],
        [[2, 6], [3, 20], [4, 3]],
        [[3, 14]],
        [[4, 2]],
        [],
        [],
    ]
    print(dijkstras_algorithm(start, edges))


if __name__ == "__main__":
    main()
