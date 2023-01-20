"""
Given a string, sort it based on the decreasing frequency of its characters.
Example 1:
I/P: "Programming"
O/P: "rrggmmPiano"
Explanation: 'r', 'g' and 'm' appeared twice, so they need to appear before any other character.

Example 2:
I/P: "abcbab"
O/P: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.

Time: The time complexity of the above algorithm is O(D * logD) where 'D' is the number of distinct characters in the
        input string. This means, in the worst case, when all characters are unique the time complexity of the
        algorithm will be O(N *logN) where 'N' is the total number of characters in the string.
Space: The space complexity will be O(N), as in the worst case, we need to store all the 'N' characters in the HashMap.
"""
from heapq import *


def sort_character_by_frequency(str):

    # find the frequency of each character
    char_frequency_map = {}
    for char in str:
        char_frequency_map[char] = char_frequency_map.get(char, 0) + 1

    max_heap = []
    # add all characters to the max_heap
    for char, frequency in char_frequency_map.items():
        heappush(max_heap, (-frequency, char))

    # build a string, appending the most occurring characters first
    sorted_string = []
    while max_heap:
        frequency, char = heappop(max_heap)
        for _ in range(-frequency):
            sorted_string.append(char)
    return ''.join(sorted_string)


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


if __name__ == "__main__":
    main()
