"""
Given the head of a singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
Time: Finding the cycle in a LinkedList with N nodes and also finding the length of the cycle requires O(N). We will
        need O(N) to find the start of the cycle.
Space: The algorithm runs in constant space O(1).
"""
from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    cycle_length = 0
    # find the LinkedList cycle
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            return calculate_cycle_length(slow)
    return find_start(head, cycle_length)


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


def find_start(head, cycle_length):
    pointer1 = head
    pointer2 = head
    # move pointer2 ahead 'cycle_length' nodes
    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1
    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    # print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    # print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList cycle starts: " + str(find_cycle_start(head)))

    head.next.next.next.next.next.next = head
    # print("LinkedList has cycle: " + str(has_cycle(head)))
    # print("LinkedList cycle length: " + str(find_cycle_length(head)))
    print("LinkedList cycle starts: " + str(find_cycle_start(head)))


if __name__ == "__main__":
    main()
