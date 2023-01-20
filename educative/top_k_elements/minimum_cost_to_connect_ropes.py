"""
Given 'N' ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. The cost of
connecting two ropes is equal to the sum of their lengths.
Example 1:
I/P: [1, 3, 11, 5]
O/P: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4 + 9 + 20).

Example 2:
I/P: [3, 4, 5, 6]
O/P: 36
Explanation: First connect 3+4(=7), then 5+6(=11), 7+11(=18). Total cost is 36 (7+11+18)

Example 3:
I/P: [1, 3, 11, 5, 2]
O/P: 42
Explanation: First connect 1+2(=3), then 3+3(=6), 6+5(=11), 11+11(=22). Total cost is 42 (3+6+11+22)

Time: Given 'N' ropes, we need O(N*logN) to insert all the ropes in the heap. In each step, while processing the heap,
    we take out two elements from the heap and insert one. This means we will have a total of 'N' steps, having a total
    time complexity of O(N*logN)

Space: The space complexity will be O(N) because we need to store all the ropes in the heap.
"""
from heapq import *


def minimum_cost_to_connect_ropes(rope_lengths):
    min_heap = []
    # add all ropes to the min_heap
    for i in rope_lengths:
        heappush(min_heap, i)

    # go through the values of the heap, in each step take top (lowest) rope_lengths from the min_heap
    # connect them and push the result back to the min_heap.
    # keep doing this until the heap is left with only one rope
    result, temp = 0, 0
    while len(min_heap) > 1:
        temp = heappop(min_heap) + heappop(min_heap)
        result += temp
        heappush(min_heap, temp)
    return result


def main():
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


if __name__ == "__main__":
    main()
