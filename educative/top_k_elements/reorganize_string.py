"""
Given a string and a number 'K', find if the string can be rearranged such that the same characters are at least
'K' distance apart from each other.

Example 1:
I/P: "mmpp", K = 2
O/P: "mpmp" or "pmpm"
Explanation: All same characters are 2 distance apart.

Example 2:
I/P: "Programming", K = 3
O/P: "rgmProgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
Explanation: All same characters are 3 distance apart.

Example 3:
I/P: "aab", K = 2
O/P: "aba"
Explanation: All same characters are 2 distance apart.

Example 4:
I/P: "aappa", K = 3
O/P: ""
Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.

Time: The time complexity of the above algorithm is O(N*logN) where 'N' is the number of characters in the input string.
Space: The space complexity will be O(N), as in the worst case, we need to store all the 'N' characters in the HashMap.
"""
from heapq import *
from collections import deque


def reorganize_string(str, k):
    if k <= 1:
        return str

    char_frequency_map = {}
    for char in str:
        char_frequency_map[char] = char_frequency_map.get(char, 0) + 1

    max_heap = []
    # add all characters to the max heap
    for char, frequency in char_frequency_map.items():
        heappush(max_heap, (-frequency, char))

    queue = deque()
    result_string = []
    while max_heap:
        frequency, char = heappop(max_heap)
        # append the current character to the result string and decrement its count
        result_string.append(char)
        # decrement the frequency and append to the queue
        queue.append((char, frequency + 1))
        if len(queue) == k:
            char, frequency = queue.popleft()
            if -frequency > 0:
                heappush(max_heap, (frequency, char))
    # if we were successful in appending all the characters to the result string, return it
    return ''.join(result_string) if len(result_string) == len(str) else ""


def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


if __name__ == "__main__":
    main()
