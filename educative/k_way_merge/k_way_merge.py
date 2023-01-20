"""
Given an array of 'K' sorted LinkedLists, merge them into one sorted list.
I/P: L1 = [2, 6, 8], L2 = [3, 6, 7], L3 = [1, 3, 4]
O/P: [1, 2, 3, 3, 4, 6, 6, 7, 8]

I/P: L1 = [5, 8, 9], L2 = [1, 7]
O/P: [1, 5, 7, 8, 9]

Time: Since we'll be going through all the elements of all arrays and will be removing/adding one element to the heap in
    each step, the time complexity of the above algo will be O(N*logK), where 'N' is the total number of elements in all
    the 'K' input arrays.

Space: The space complexity will be O(K) because, at any time, our min-heap will be storing one number from all the 'K'
    input arrays.
"""
from __future__ import print_function
from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    min_heap = []
    # put the root of each list in the min heap
    for root in lists:
        if root is not None:
            heappush(min_heap, root)

    # take the smallest(top) element from the min-heap and add it to the result
    # if the top element has a next element, add it the heap
    result_head, result_tail = None, None
    while min_heap:
        node = heappop(min_heap)
        if result_head is None:
            result_head = result_tail = node
        else:
            result_tail.next = node
            result_tail = result_tail.next
        if node.next is not None:
            heappush(min_heap, node.next)
    return result_head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements from the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next


if __name__ == "__main__":
    main()
