"""
We are given a list of Jobs. Each job has a Start time, an End time and a CPU load when it is running. Our goal is to
find the maximum CPU load at any time if all the jobs are running on the same machine.
Example1:
Jobs: [[1, 4, 3], [2, 5, 4], [7, 9, 6]]
Output: 7
Explanation: Since [1, 4, 3] and [2, 5, 4] overlap, their maximum CPU load (3 + 4 = 7) will be when both the jobs are
            running at the same time i.e., during the time interval (2, 4)

Time: O(N*logN)
Space: O(N)
"""
from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # min heap based on the job.end
        return self.end < other.end


def find_max_cpu_load(jobs):
    # sort the jobs by start time
    jobs.sort(key=lambda x: x.start)
    max_cpu_load, current_cpu_load = 0, 0
    min_heap = []

    for j in jobs:
        # remove all the jobs that have ended
        while len(min_heap) > 0 and j.start >= min_heap[0].end:
            current_cpu_load -= min_heap[0].cpu_load
            max_cpu_load = max(max_cpu_load, current_cpu_load)
            heappop(min_heap)
        # add the current job into min_heap
        heappush(min_heap, j)
        current_cpu_load += j.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)
    return max_cpu_load


def main():
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))


if __name__ == "__main__":
    main()
