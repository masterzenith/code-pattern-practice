"""
Given an array of points in a 2D plane, find 'K' closest points to the origin.
I/P: points = [[1, 2], [1, 3]], K = 1
O/P: [[1, 2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

Example 2:
I/P: point = [[1, 3], [3, 4], [2, -1]], K = 2
O/P: [[1, 3], [2, -1]]

Time: Time complexity of this algorithm is O(N*logK) as we iterating all points and pushing them into the heap.
space: The space complexity will be O(K) because we need to store 'K' point in the heap.
"""
from __future__ import print_function
from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # used for max_heap
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "]", end='')


def find_closest_points(points, k):
    max_heap = []
    # put first 'k' points in the max_heap
    for i in range(k):
        heappush(max_heap, points[i])

    # go through the remaining points of the input array, if a point is closer to the origin than the top point of the
    # max_heap, remove the top point from heap and add the point from the input array
    for i in range(k, len(points)):
        if points[i].distance_from_origin() < max_heap[0].distance_from_origin():
            heappop(max_heap)
            heappush(max_heap, points[i])

    # the heap has 'k' points closest to the origin, return them in a list
    return list(max_heap)


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


if __name__ == "__main__":
    main()
