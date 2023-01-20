"""
Given a set of n number of tasks, implement a task scheduler method, tasks(), to run in O(nlogn) time that finds the
minimum number of machines required to complete these n tasks.
Constraints:
Task start time <= Task end time

I/P: T = [(1, 7), (8, 13), (5, 6), (10, 14), (6, 7)]
O/P: Optimal machines required = 2
In this example, only 2 machines are required to execute all the input tasks.

I/P: T = [(2, 5), (2, 5), (2, 5), (2, 5)]
O/P: optimal machines required = 4
4 machines are required to execute all the input tasks.

I/P: T = [(2, 3), (4, 7), (8, 18), (19, 25), (26, 30)]
O/P: Optimal machines required = 1
Only 1 machine is required to execute all the input tasks.
"""
# Task Scheduler - LeetCode 621 similar
import heapq


def tasks(tasks_list):
    return -1