"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
I/P: String="araaci", K=2
O/P: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa"

I/P: String="araaci", K=1
O/P: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa"

I/P: String="cbbebi", K=3
O/P: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" and "bbebi"

Time: The time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N)
Space: The algorithm's space complexity is O(K), as we will be storing a maximum of 'K + 1' characters in the
    hashmap.
"""


def longest_substring_with_k_distinct(str, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1   # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


if __name__ == "__main__":
    main()
