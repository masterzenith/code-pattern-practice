"""
There are 'N' tasks, labeled from '0' to 'N-1'. Each task can have some prerequisite tasks which need to be completed
before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to
schedule all the tasks.
Example 1:
I/P: Tasks = 3, Prerequisites=[0, 1], [1, 2]
O/P: True
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish before '2' can be
            scheduled. A possible sceduling of tasks is: [0, 1, 2]

Example 2:
I/P: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
O/P: False
Explanation: The tasks have cyclic dependency, therefore they cannot be sceduled.

Example 3:
I/P: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
O/P: True
Explanation: A possible sceduling of tasks is: [0 1 4 3 2 5]

Time: In step 'd', each task can become a source only once and each edge(prerequisite) will be accessed and removed
        once. Therefore, the time complexity of the above algorithm will be O(V+E), where 'V' is the total numbers
        of tasks and 'E' is the total number of prerequisite.
Space: The space complexity will be O(V+E), since we are storing all of the prerequisite for each task in an
        adjacency list.
"""
from collections import deque


def is_sceheduling_possible(tasks, prerequisites):
    sorted_order = []
    if tasks <= 0:
        return False

    # a. Initialize the graph
    in_degree = {i: 0 for i in range(tasks)}   # count of incoming edges
    graph = {i: [] for i in range(tasks)}   # adjacency list graph

    # b. Build the graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)    # put the child into it's parent's list
        in_degree[child] += 1   # increment child's in_degree

    # c. Find all sources i.e.. all vertices with 0 in-degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sorted_order and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue.
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:   # get the node's children to decrement their in-degrees
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # if sorted_order doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we will not
    # be able to schedule all tasks
    return len(sorted_order) == tasks


def main():
    print("Is scheduling possible: " +
          str(is_sceheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_sceheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_sceheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))


if __name__ == "__main__":
    main()


"""
Course Schedule: There are 'N' courses, labeled from '0' to 'N-1'. Each course can have some prerequisite courses which 
need to be completed before it can be taken. Given the number of courses and a list of prerequisite pairs, find if it is 
possible for a student to take all the courses.
Solution: This problem is exactly similar to our parent problem. In this problem, we have courses instead of tasks.
"""