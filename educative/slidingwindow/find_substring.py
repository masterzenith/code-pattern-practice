"""
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given
pattern.
I/P: String="aabdec", Pattern="abc"
O/P: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

I/P: String="abdbca", Pattern="abc"
O/P: "bca"
Explanation: The smallest substring having all the characters of the pattern is "bca"

I/P: String="adcad", Pattern="abc"
O/P: ""
Explanation: No substring in the given string has all characters of the pattern.

Time: The time complexity of the above algo will be O(N+M) where 'N' and 'M' are the number of characters in the input
string and the patten respectively.

Space: The space complexity of the algo is O(M) since in the worst case, the whole pattern can have distinct characters
    which will go into the HashMap. In the worst case, we also need O(N) space for the resulting substring, which will
    happen when the input string is a permutation of the pattern.
"""


def find_substring(str1, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str1) + 1
    char_frequency = {}
    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # our goal is to match all the characters from the 'char_frequency' with the current window try to extend the range
    # [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:  # Count every matching of a character
                matched += 1
        # Shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1
            # Note that we could have redundant matching characters, therefore we'll decrement the matched count only
            # when a useful occurrence of a matched character is going out of the window
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    if min_length > len(str1):
        return ""
    return str1[substr_start: substr_start + min_length]


def main():
    print('The smallest substring having all the characters of the pattern is: ' + str(find_substring("aabdec", "abc")))
    print('The smallest substring having all the characters of the pattern is: ' + str(find_substring("abdbca", "abc")))
    print('The smallest substring having all the characters of the pattern is: ' + str(find_substring("adcad", "abc")))


if __name__ == "__main__":
    main()
