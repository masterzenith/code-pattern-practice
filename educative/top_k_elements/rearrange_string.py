"""
Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.
Example 1:
I/P: "aappp"
O/P: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.

Example 2:
I/P: "Programming"
O/P: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.

Example 3:
I/P: "aapa"
O/P: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".

Time: The time complexity of the above algorithm is O(N*logN) where 'N' is the number of characters in the input
        string.
Space: The space complexity will be O(N), as in the worst case, we need to store all the 'N' characters in the HashMap.
"""
from heapq import *


def rearrange_string(str):
    char_frequency_map = {}
    for char in str:
        char_frequency_map[char] = char_frequency_map.get(char, 0) + 1

    max_heap = []
    # add all the characters to the max_heap
    for char, frequency in char_frequency_map.items():
        heappush(max_heap, (-frequency, char))

    previous_char, previous_frequency = None, 0
    result_string = []
    while max_heap:
        frequency, char = heappop(max_heap)
        # add the previous entry back in the heap if its frequency is greater than zero
        if previous_char and -previous_frequency > 0:
            heappush(max_heap, (previous_frequency, previous_char))
        # append the current character to the result string and decrement its count
        result_string.append(char)
        previous_char = char
        previous_frequency = frequency + 1  # decrement the frequency
    # if we were successful in appending all the characters to the result string, return it
    return ''.join(result_string) if len(result_string) == len(str) else ""


def main():
    print("Rearranged string: " + rearrange_string("aaapp"))
    print("Rearranged string: " + rearrange_string("Programming"))
    print("Rearranged string: " + rearrange_string("aapa"))


if __name__ == "__main__":
    main()
