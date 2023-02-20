"""
Rearrange Linked List
Write a function that takes in the head of a Singly Linked List and an integer k, rearranges the list in place (i.e.,
doesn't create a brand new list) around nodes with value k, and returns its new head.
Rearranging a Linked List around nodes with value k means moving all nodes with a value smaller than k before all nodes
with value k and moving all nodes with a value greater than k after all nodes with value k.
All moved nodes should maintain their original relative ordering if possible.
Note that the linked list should be rearranged even if it doesn't have any nodes with value k.
Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null
if it's the tail of the list.
You can assume that the input Linked List will always have at least one node; in other words, the head will never be None
/ null.
Sample Input:
head = 3 -> 0 -> 5 -> 2 -> 1 -> 4 // the head node with value 3
k = 3

Sample Output:
0 -> 2 -> 1 -> 3 -> 5 -> 4 // the new head node with value 0
// Note that the nodes with values 0, 2, and 1 have
// maintained their original relative ordering, and
// so have the nodes with values 5 and 4.

Hints:
1. The final linked list that you have to return essentially consists of three linked lists attached to one another: one
with nodes whose values are smaller than k, one with nodes whose values are equal to k, and one with nodes whose values
are greater than k.
2. Iterate through the linked list once, build the three linked lists mentioned in Hint #1 as you go, and finally connect
these three linked lists to form the rearranged list.
3. To build the three linked lists mentioned in Hints #1 and #2, you'll have to keep track of their heads and tails and
update the appropriate linked list's tail with each node that you traverse as you iterate through the main linked list.
You can determine which linked list is the relevant one by simply comparing the value of the node that you're traversing
to k.
4. Connecting the three linked lists mentioned in the previous Hint won't be as simple as it sounds, mainly because one
or two of the linked lists might actually be empty, depending on the various nodes' values and the value of k.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the number of nodes in the Linked List
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(N) time and O(1) space
def rearrange_linked_list(head, k):
    head_of_small = None
    pointer_small = None
    head_of_large = None
    pointer_large = None
    current = head
    node_with_value_k = None
    pointer_node_with_value_k = None

    while current is not None:
        if current.value < k:
            if head_of_small is None:
                head_of_small = current
                pointer_small = current
            else:
                pointer_small.next = current
                pointer_small = pointer_small.next
        elif current.value == k:
            if node_with_value_k is None:
                node_with_value_k = current
                pointer_node_with_value_k = current
            else:
                pointer_node_with_value_k.next = current
                pointer_node_with_value_k = pointer_node_with_value_k.next
        else:
            if head_of_large is None:
                head_of_large = current
                pointer_large = current
            else:
                pointer_large.next = current
                pointer_large = pointer_large.next
        current = current.next

    if pointer_large is not None:
        pointer_large.next = None

    if node_with_value_k is None:
        if pointer_small is None:
            return head_of_large
        else:
            pointer_small.next = head_of_large
            return head_of_small
    else:
        if pointer_small is None:
            pointer_node_with_value_k.next = head_of_large
            return node_with_value_k
        else:
            pointer_small.next = node_with_value_k
            pointer_node_with_value_k.next = head_of_large
            return head_of_small


def main():
    head = LinkedList(3)
    head.next(0)
    head.next.next(5)
    head.next.next.next(2)
    head.next.next.next.next(1)
    head.next.next.next.next.next(4)
    k = 3
    print(rearrange_linked_list(head, k))


if __name__ == "__main__":
    main()