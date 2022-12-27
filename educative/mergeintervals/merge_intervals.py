"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive
intervals.
Intervals: [[1, 4], [2, 5], [7, 9]]
O/P: [[1, 5], [7, 9]]

Intervals: [[6, 7], [2, 4], [5, 9]]
O/P: [[2, 4], [5, 9]]
Explanation: Since the intervals [6, 7] and [5, 9] overlap, we merged them into one [5, 9].

Time: The time complexity will be O(N*logN), where N is the total number of intervals. We are iterating the intervals
    only once which will take O(N), in the beginning though, since we need to sort the intervals, our algorithm will
    take O(N*logN)
Space: The space complexity will be O(N), because we need O(N) space for sorting

Similar Problem: Given a set of intervals, find out if any two intervals overlap.
Example:
    Intervals: [[1, 4], [2, 5], [7, 9]]
    Output: true
    Explanation: Intervals [1, 4] and [2, 5] overlap
"""
from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals on the start time
    intervals.sort(key=lambda x: x.start)

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:   # overlapping intervals, adjust the 'end'
            end = max(interval.end, end)
        else:   # non-overlapping interval, add the previous interval and reset
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    # add the last interval
    merged_intervals.append(Interval(start, end))
    return merged_intervals


def main():
    print("Merged intervals: ", end='')
    for i in merge_intervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge_intervals([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge_intervals([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


if __name__ == "__main__":
    main()
