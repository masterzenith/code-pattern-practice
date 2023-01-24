"""
There are 'N' tasks, labeled from '0' to 'N-1'. Each task can have some prerequisite tasks which need to be completed
before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all
possible ordering of tasks meeting all prerequisites.
Example 1:
I/P: Tasks=3, Prerequisites=[0, 1], [1, 2]
O/P: [0, 1, 2]
Explanation: There is only possible ordering of the tasks.

Example 2:
I/P: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
O/P:
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all prerequisites.

Example 3:
I/P: Tasks=6, prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
O/P:
1) [0, 1, 4, 3, 2, 5]
2) [0, 1, 3, 4, 2, 5]
3) [0, 1, 3, 2, 4, 5]
4) [0, 1, 3, 2, 5, 4]
5) [1, 0, 3, 4, 2, 5]
6) [1, 0, 3, 2, 4, 5]
7) [1, 0, 3, 2, 5, 4]
8) [1, 0, 4, 3, 2, 5]
9) [1, 3, 0, 2, 4, 5]
10) [1, 3, 0, 2, 5, 4]
11) [1, 3, 0, 4, 2, 5]
12) [1, 3, 2, 0, 5, 4]
13) [1, 3, 2, 0, 4, 5]

Time: If we don't have any prerequisite, all combinations of the tasks can represent a topological ordering. As we know,
        that there can be N! combinations for 'N' numbers, therefore the time and space complexity of our algorithm will
        be O(V! * E) where 'V' is the total number of tasks and 'E' is the total prerequisites. We need the 'E' part
        because in each recursive call, at max, we remove (and add back) all the edges.
"""
from collections import deque


def print_order(tasks, prerequisites):
    sorted_order = []
    if tasks <= 0:
        return False

    # a. Initialize the graph
    in_degree = {i: 0 for i in range(tasks)}   # count of incoming edges
    graph = {i: [] for i in range(tasks)}   # adjacency list graph

    # b. build the graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)     # put the child into it's parent's list
        in_degree[child] += 1    # increment child's in_degree

    # c. Find all sources i.e.., all vertices with 0 in_degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)
    print_all_topological_sorts(graph, in_degree, sources, sorted_order)


def print_all_topological_sorts(graph, in_degree, sources, sorted_order):
    if sources:
        for vertex in sources:
            sorted_order.append(vertex)
            sources_for_next_call = deque(sources)  # make a copy of sources
            # only remove the current source, all other sources should remain in the queue for the next call
            sources_for_next_call.remove(vertex)

            for child in graph[vertex]:   # get the node's children to decrement their in-degrees
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources_for_next_call.append(child)

        # recursive call to print other orderings from the remaining (and new) sources
        print_all_topological_sorts(graph, in_degree, sources_for_next_call, sorted_order)
        # backtrack remove the vertex from the sorted order and put all of its children back to consider
        # the next source instead of the current vertex
        sorted_order.remove(vertex)
        for child in graph[vertex]:
            in_degree[child] += 1
    # if sorted_order doesn't contain all tasks, either we've a cyclic dependency between tasks, or
    # we have not processed all the tasks in this recursive call
    if len(sorted_order) == len(in_degree):
        print(sorted_order)


def main():
    print("Is scheduling possible: " + str(print_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " + str(print_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " + str(print_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


if __name__ == "__main__":
    main()

