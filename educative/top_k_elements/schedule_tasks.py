"""
You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU interval to
execute but once a task has finished, it has a cooling period during which it can't be run again. If the cooling period
for all tasks is 'K' intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.
If at any time the server can't execute any task then it must stay idle.

Example 1:
I/P: [a, a, a, b, c, c], K = 2
O/P: 7
Explanation: a -> c -> b -> a -> c -> idle -> a

Example 2:
I/P: [a, b, a], K = 3
O/P: 5
Explanation: a -> b -> idle -> idle -> a

Time: The time complexity of the above algorithm is O(N*logN) where 'N' is the number of tasks. Our while loop will
    iterate once for each occurrence of the task in the input(i.e. 'N') and in each iteration we will remove a task
    from the heap which will take O(logN) time. Hence the overall time complexity of our algorithm is O(N*logN)
Space: The space complexity will be O(N), as in the worst case, we need to store all the 'N' tasks in the HashMap
"""
from heapq import *


def schedule_tasks(tasks, k):
    interval_count = 0
    task_frequency_map = {}
    for char in tasks:
        task_frequency_map[char] = task_frequency_map.get(char, 0) + 1
    max_heap = []
    # add all tasks to the max_heap
    for char, frequency in task_frequency_map.items():
        heappush(max_heap, (-frequency, char))

    while max_heap:
        wait_list = []
        n = k + 1  # try to execute as many as 'k+1' tasks from the max-heap
        while n > 0 and max_heap:
            interval_count += 1
            frequency, char = heappop(max_heap)
            if -frequency > 1:
                # decrement the frequency and add to the wait_list
                wait_list.append((frequency+1, char))
            n -= 1
        # put all the waiting list back on the heap
        for frequency, char in wait_list:
            heappush(max_heap, (frequency, char))
        if max_heap:
            interval_count += n   # we'll be having 'n' idle intervals for the next iteration
    return interval_count


def main():
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))


if __name__ == "__main__":
    main()
