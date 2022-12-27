"""
For 'K' employees we are given a list of intervals representing each employee's working hours. Our goal is to determine
if there is a free interval which is common to all employees. You can assume that each list of employee working hours
is sorted on the start time.
Example1:
I/P: Employee working hours=[[1, 3], [5, 6]], [[2, 3], [6, 8]]
O/P: [3, 5]
Explanation: All the employees are free between [3, 5]

Time: O(N*logK) where N is the total number of intervals, and K is the total number of employees. This is because
        we are iterating through the intervals only once(which will take O(N)), and everytime we process an interval,
        we remove and can insert one interval in the Min Heap,(which will take O(logK)). At any time, the heap will not
        have more than K elements.
Space: At any time, the heap will not have more than K elements. So, O(K)

"""
from __future__ import print_function

from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employee_index = employee_index
        self.interval_index = interval_index  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on interval.start
        self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    result, min_heap = [], []

    # insert the first interval of each employee to the queue
    for i in range(n):
        heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))
    previous_interval = min_heap[0].interval
    while min_heap:
        queue_top = heappop(min_heap)
        # if previous_interval is not overlapping with the next interval, insert a free interval
        if previous_interval.end < queue_top.interval.start:
            result.append(Interval(previous_interval.end, queue_top.interval.start))
            previous_interval = queue_top.interval
        else:
            # overlapping intervals, update the previous_interval if needed
            if previous_interval.end < queue_top.interval.end:
                previous_interval = queue_top.interval
                # if there are more intervals available for the same employee add their next interval

        employee_schedule = schedule[queue_top.employee_index]
        if len(employee_schedule) > queue_top.interval_index + 1:
            heappush(min_heap, EmployeeInterval(employee_schedule[queue_top.interval_index + 1],
                                                queue_top.employee_index, queue_top.interval_index + 1))
    return result


def main():
    input_intervals = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    print("Free Intervals: ", end='')
    for interval in find_employee_free_time(input_intervals):
        interval.print_interval()
    print()


if __name__ == "__main__":
    main()
