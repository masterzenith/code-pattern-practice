"""
Sort K-Sorted Array
Write a function that takes in a non-negative integer k and a k-sorted array of integers and returns the sorted version
of the array. Your function can either sort the array in place or create an entirely new array.
A k-sorted array is a partially sorted array in which all elements are at most k positions away from their sorted position.
For example, the array [3, 1, 2, 2] is k-sorted with k = 3, because each element in the array is at most 3 positions away
from its sorted position.
Note that you're expected to come up with an algorithm that can sort the k-sorted array faster than in O(nlog(n)) time.

Sample Input:
array = [3, 2, 1, 5, 4, 7, 6, 5]
k = 3
Sample Output:
[1, 2, 3, 4, 5, 5, 6, 7]

Hints:
1. What does the k parameter tell you? How can you use it to come up with an algorithm that runs in O(nlog(k))?
2. Since the input array is k-sorted, try repeatedly sorting k elements at a time and inserting the minimum element of
all those k elements into its final sorted position in the array.
3. What auxiliary data structure would be helpful to quickly determine the minimum element of k elements?
4. As you iterate through the array, use a min-heap to keep track of the most recent k elements. At each iteration,
remove the minimum value from the heap, insert it into its final sorted position in the array, and add the current element
in the array to the heap. Continue this process until the heap is empty.

Optimal Space & Time Complexity
O(nlog(k)) time | O(k) space - where n is the number of elements in the array and k is how far away elements are from
their sorted position

Other Solution:
https://github.com/das-jishu/algoexpert-data-structures-algorithms/blob/master/Hard/sort-k-sorted-array.py
"""


def sort_k_sorted_array(array, k):
    heap = MinHeap(array[:min(k + 1, len(array))])
    index = 0
    while not heap.is_empty():
        min_element = heap.remove()
        array[index] = min_element
        index += 1
        if index + k < len(array):
            heap.insert(array[index + k])
    return array


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
    array = [3, 2, 1, 5, 4, 7, 6, 5]
    k = 3
    print(sort_k_sorted_array(array, k))


if __name__ == "__main__":
    main()
