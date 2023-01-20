"""
Design a class to efficiently find the Kth largest element in a stream of numbers.
The class should have the following two things:
1. The constructor of the class should accept an integer array containing initial numbers from the stream and an
    integer 'K'.
2. The class should expose a function add(int num) which will store the given number and return the Kth largest number.

Time: The time complexity of the add() function will be O(logK) since we are inserting the new number in the heap.
Space: The space complexity will be O(K) for storing numbers in the heap.
"""
from heapq import *


class KthLargestNumberInStream:
    min_heap = []

    def __init__(self, nums, k):
        self.k = k
        # add the numbers in the min_heap
        for num in nums:
            self.add(num)

    def add(self, num):
        # add the new number in the min_heap
        heappush(self.min_heap, num)

        # if heap has more than 'k' numbers, remove one number
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

        # return the Kth largest number
        return self.min_heap[0]


def main():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


if __name__ == "__main__":
    main()

