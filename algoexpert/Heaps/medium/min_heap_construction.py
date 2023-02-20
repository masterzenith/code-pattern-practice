"""
Min Heap Construction
Implement a MinHeap class that supports:
- Building a Min Heap from an input array of integers.
- Inserting integers in the heap.
- Removing the heap's minimum / root value.
- Peeking at the heap's minimum / root value.
- Sifting integers up and down the heap, which is to be used when inserting and removing values.
Note that the heap should be represented in the form of an array.
If you're unfamiliar with Min Heaps, we recommend watching the Conceptual Overview section of this question's video
explanation before starting to code.

Sample Usage:
array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

// All operations below are performed sequentially.
MinHeap(array): - // instantiate a MinHeap (calls the buildHeap method and populates the heap)
buildHeap(array): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
insert(76): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
peek(): -5
remove(): -5 [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
peek(): 2
remove(): 2 [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]
peek(): 6
insert(87): - [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]

Hints:
1. For the buildHeap(), remove(), and insert() methods of the Heap, you will need to use the siftDown() and siftUp()
methods. These two methods should essentially allow you to take any node in the heap and move it either down or up in the
heap until it's in its final, appropriate position. This can be done by comparing the node in question to its child nodes
in the case of siftDown() or to its parent node in the case of siftUp().
2. In an array-based Heap, you can easily access a node's children nodes and parent node by using the nodes' indices.
If a node is located at index i, then its children nodes are located at indices 2 * i + 1 and 2 * i + 2, and its parent
node is located at index Math.floor((i - 1) / 2).
3. To implement the buildHeap() method, you can either sift every node in the input array down to its final, correct
position, or you can sift every node in the input array up to its final, correct position. What are the runtime
implications of both approaches? Which methods (siftDown() or siftUp()) will insert() and remove() utilize? What about
peek()?

Optimal Space & Time Complexity
BuildHeap: O(n) time | O(1) space - where n is the length of the input array SiftDown: O(log(n)) time | O(1) space -
where n is the length of the heap SiftUp: O(log(n)) time | O(1) space - where n is the length of the heap Peek: O(1) | O(1)
Remove: O(log(n)) time | O(1) space - where n is the length of the heap Insert: O(log(n)) time | O(1) space - where n is
the length of the heap.

https://github.com/lee-hen/Algoexpert/tree/master/medium/21_heap_construction#hints
"""


class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    def is_empty(self):
        return len(self.heap) == 0

    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array

    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if heap[idx_to_swap] < heap[current_idx]:
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return

    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[current_idx] < heap[parent_idx]:
            self.swap(current_idx, parent_idx, heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


def main():
    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    min_heap = MinHeap(array)
    print(min_heap.build_heap(array))
    print("insertion is done: " + str(min_heap.insert(76)))
    print(min_heap.peek())
    print(min_heap.remove())
    print(min_heap.peek())
    print(min_heap.remove())
    print(min_heap.peek())
    print("insertion is done: " + str(min_heap.insert(87)))


if __name__ == "__main__":
    main()
