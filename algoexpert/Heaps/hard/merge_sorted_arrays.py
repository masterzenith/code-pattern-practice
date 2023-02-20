"""
Merge Sorted Arrays
Write a function that takes in a non-empty list of non-empty sorted arrays of integers and returns a merged list of all
of those arrays.
The integers in the merged list should be in sorted order.

Sample Input:
arrays = [
    [1, 5, 9, 21],
    [-1, 0],
    [-124, 81, 121],
    [3, 6, 12, 20, 150],
]
Sample Output:
[-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]

Hints:
1. If you were given just two sorted lists of numbers in real life, what steps would you take to merge them into a single
sorted list? Apply the same process to k sorted lists.
2. The first element in each array is the smallest element in the respective array; to find the first element to add to
the final sorted list, pick the smallest integer out of all of the smallest elements. Once you've found the smallest
integer, move one position forward in the array that it came from and continue applying this logic until you run out of
elements.
3. The approach described in Hint #2 involves repeatedly finding the smallest of k elements, since there are k arrays.
Doing so can be naively implemented using a simple loop through the k relevant elements, which results in an O(k)-time
operation. Can you speed up this operation by using a specific data structure that lends itself to quickly finding the
minimum value in a set of values.
4. Follow the approach described in Hint #2, using a Min Heap to store the k smallest elements at any given point in your
algorithm.

Optimal Space & Time Complexity
O(nlog(k) + k) time | O(n + k) space - where n is the total number of array elements and k is the number of arrays

Other solution:
https://github.com/das-jishu/algoexpert-data-structures-algorithms/blob/master/Very%20Hard/merge-sorted-arrays.py
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
            if child_two_idx != -1 and heap[child_two_idx]["num"] < heap[child_one_idx]["num"]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if heap[idx_to_swap]["num"] < heap[current_idx]["num"]:
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return

    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[current_idx]["num"] < heap[parent_idx]["num"]:
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


def merge_sorted_arrays(arrays):
    merged_array = []
    smallest = []
    for idx in range(len(arrays)):
        smallest.append({"array_idx": idx, "elem_idx": 0, "num": arrays[idx][0]})
    min_heap = MinHeap(smallest)
    while not min_heap.is_empty():
        smallest_element = min_heap.remove()
        merged_array.append(smallest_element["num"])
        array_idx = smallest_element["array_idx"]
        element_idx = smallest_element["elem_idx"]
        if element_idx >= len(arrays[array_idx]) - 1:
            continue
        min_heap.insert({"array_idx": array_idx, "elem_idx": element_idx + 1, "num": arrays[array_idx][element_idx + 1]})
    return merged_array


def main():
    arrays = [
        [1, 5, 9, 21],
        [-1, 0],
        [-124, 81, 121],
        [3, 6, 12, 20, 150],
    ]
    print(merge_sorted_arrays(arrays))


if __name__ == "__main__":
    main()