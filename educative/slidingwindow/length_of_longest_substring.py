"""
Given a string with lowercase letters only, if you are allowed to replace no more than 'k' letters with any letter,
find the length of the longest substring having the same letters after replacement.

I/P: String="aabccbb", k=2
O/P: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

I/P: String="abbcb", k=1
O/P: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

I/P: String="abccde", k=1
O/P: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

Time: The above algorithm's time complexity will be O(N), where 'N' is the number of letters in the input string.
Space: we have 26 lower case letters so, asymptotically space complexity will be O(1).
"""


def length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])
        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one
        # letter repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window as we aren't
        # allowed to replace more than 'k' letters.
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


if __name__ == "__main__":
    main()
