"""
Given the head of a singly Linkedlist, write a function to determine if the LinkedList has a cycle in it or not.
Time: O(N) where N is the total number of nodes in the LinkedList
Space: The algorithm runs in constant space O(1)

Given the head of a LinkedList with a cycle, find the length of the cycle.
Time: O(N) where N is the total number of nodes in the LinkedList
Space: The algorithm runs in constant space O(1)
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True     # found the cycle
    return False


def find_cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:    # found the cycle
            return calculate_cycle_length(slow)
    return 0


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


if __name__ == "__main__":
    main()

