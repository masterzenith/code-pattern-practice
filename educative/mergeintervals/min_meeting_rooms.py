"""
Given a list of intervals representing the start and end time of 'N' meetings, find the minimum number of rooms
required to hold all the meetings.
Example1:
Meetings: [[1, 4], [2, 5], [7, 9]]
Output: 2
Explanation: Since [1, 4] and [2, 5] overlap, we need two rooms to hold these two meetings. [7, 9] can occur in any of
            the two rooms later.

Time: O(N*logN), where N is the total number of meetings. This is due to the sorting that we did in the beginning.
    Also, while iterating the meetings we might need to poll/offer meeting to the priority queue. Each of these
    operations can take O(logN).
Space: The space complexity of the above algorithm will be O(N) which is required for sorting.

Similar Problem:
Problem 1: Given a list of intervals, find the point where the maximum number of intervals overlap.
Problem 2: Given a list of intervals representing the arrival and departure times of trains to a train station,
            our goal is to find the minimum number of platforms required for the train station so that no train has to
            wait
"""
from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


def min_meeting_rooms(meetings):
    # sort the meetings by start time
    meetings.sort(key=lambda x: x.start)

    min_rooms = 0
    min_heap = []
    for meeting in meetings:
        # remove all the meetings that have ended
        while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heappop(min_heap)
            # add the current meeting into min_heap
        heappush(min_heap, meeting)
        # all active meetings are in the min_heap, so we need rooms for all of them.
        min_rooms = max(min_rooms, len(min_heap))
    return min_rooms


def main():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4),
                                                                      Meeting(3, 5)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))


if __name__ == "__main__":
    main()
