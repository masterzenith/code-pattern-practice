"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arraning of the characters of the string. For example, "abc" has the following six
permutations:
1. abc
2. acb
3. bac
4. cab
5. cba
6. bca
If a string has 'n' distinct characters, it will have n! permutations.
I/P: String="oidbcaf", Pattern="abc"
O/P: true
Explanation: The string contains "bca" which is a permutation of the given pattern

I/P: String="odicf", Pattern="dc"
O/P: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Time: O(N+M) where N and M are the number of characters in the input string and the pattern respectively
Space: O(M) in the worst case, the whole pattern can have distinct characters that will go into the HashMap.
"""


def find_permutation(str1, pattern):
    window_start, matched = 0, 0
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
            if char_frequency[right_char] == 0:
                matched += 1
        if matched == len(char_frequency):
            return True

        # Shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return False


def main():
    print('Permutation exists: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exists: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exists: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exists: ' + str(find_permutation("aaacb", "abc")))


if __name__ == "__main__":
    main()
