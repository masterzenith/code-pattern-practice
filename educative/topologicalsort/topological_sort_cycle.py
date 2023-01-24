"""
Topological sort of a directed graph (a graph with unidirected edges) is a linear ordering of its vertices such that for
every directed edge(U, V) from vertex U to vertex V, U comes before V in the ordering.
Given a directed graph, find if it has a cycle in it or not.

Solution: If we can't determine the topological ordering of all the vertices of a directed graph, the graph has a cycle
            in it. This was also referred to in the above code:

            if ()
Example 1:
I/P: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
O/P: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0

Example 2:
I/P: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
O/P: Following are the two valid topological sorts for the given graph:
1) 4, 2, 3, 0, 1
2) 4, 3, 2, 0, 1
3) 4, 3, 2, 1, 0
4) 4, 2, 3, 1, 0
5) 4, 2, 0, 3, 1

Example 2:
I/P: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
O/P: Following are the all valid topological sorts for the given graph:
1) 5, 6, 3, 4, 0, 1, 2
2) 6, 5, 3, 4, 0, 1, 2
3) 5, 6, 4, 3, 0, 2, 1
4) 6, 5, 4, 3, 0, 1, 2
5) 5, 6, 3, 4, 0, 2, 1
6) 5, 6, 3, 4, 1, 2, 0
There are other valid topological ordering of the graph too.

Time: In step 'd', each vertex will become a source only once and each edge will be accessed and removed once. Therefore
    the time complexity of the above algorithm will be O(V+E), where 'V' is the total number of vertices and 'E' is the
    total number of edges in the graph.
Space: The space complexity will be O(V+E), since we are storing all of the edges for each vertex in an adjacency list.
"""
from collections import deque


def topological_sort(vertices, edges):
    sorted_order = []
    if vertices <= 0:
        return sorted_order

    # a. Initialize the graph
    in_degree = {i: 0 for i in range(vertices)}    # count of incoming edges
    graph = {i: [] for i in range(vertices)}    # adjacency list graph

    # b. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)     # put the child into it's parent's list
        in_degree[child] += 1   # increment child's in_degree

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sorted_order and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:   # get the node's children to decrement their in-degrees
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sorted_order) != vertices:
        return []
    return sorted_order


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 1], [2, 6]])))


if __name__ == "__main__":
    main()
