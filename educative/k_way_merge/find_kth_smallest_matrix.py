"""
Given an N*N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the
matrix.
I/P: Matrix = [
    [2, 6, 8],
    [3, 7, 10],
    [5, 8, 11]
    ],
    K = 5
O/P: 7

Explanation: The 5th smallest number in the matrix is 7.

Time: First, we inserted at most 'K' or one element from each of the 'N' rows, which will take O(min(K,N)). Then we went
        through at most 'K' elements in the matrix and remove/add one element in the heap in each step. As we can't have
        more than 'N' elements in the heap in any condition, therefore, the overall time complexity of the above algo
        will be O(min(K,N) + K * logN)
Space: O(N), because, in the worst case, our min-heap will be storing one number from each of the 'N' rows.
"""
from heapq import *


def find_kth_smallest(matrix, k):
    min_heap = []

    # put the 1st element of each row in the min heap
    # we don't need to push more than 'k' elements in the heap
    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))

    # take the smallest(top) element from the min heap, if the running count is equal to k, return the number
    # if the row of the top element has more elements, add the next element to the heap
    number_count, number = 0, 0
    while min_heap:
        number, i, row = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break
        if len(row) > i + 1:
            heappush(min_heap, (row[i+1], i + 1, row))
    return number


def main():
    print("Kth smallest number is: " +
          str(find_kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


if __name__ == "__main__":
    main()