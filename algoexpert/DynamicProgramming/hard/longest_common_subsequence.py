"""
Longest Common Subsequence
Write a function that takes in two strings and returns their longest common subsequence.
A subsequence of a string is a set of characters that aren't necessarily adjacent in the string but that are in the same
order as they appear in the string. For instance, the characters ["a", "c", "d"] form a subsequence of the string "abcd",
and so do the characters ["b", "d"]. Note that a single character in a string and the string itself are both valid
subsequences of the string.
You can assume that there will only be one longest common subsequence.

Sample Input:
str1 = "ZXVVYZW"
str2 = "XKYKZPW"
Sample Output
["X", "Y", "Z", "W"]

Hints:
1. Try building a two-dimensional array of the longest common subsequences of substring pairs of the input strings. Let
the rows of the array represent substrings of the second input string str2. Let the first row represent the empty string.
Let each row i thereafter represent the substrings of str2 from 0 to i, with i excluded. Let the columns similarly
represent the first input string str1.
2. Build up the array mentioned in Hint #1 one row at a time. In other words, find the longest common subsequences for
all the substrings of str1 represented by the columns and the empty string represented by the first row, then for all the
substrings of str1 represented by the columns and the first letter of str2 represented by the second row, etc., until you
compare both full strings. Find a formula that relates the longest common subsequence at any given point to previous subsequences.
3. Do you really need to build and store subsequences at each point in the two-dimensional array mentioned in Hint #1?
Try storing booleans to determine whether or not a letter at a given point in the two-dimensional array is part of the
longest common subsequence as well as pointers to determine what should come before this letter in the final subsequence.
Use these pointers to backtrack your way through the array and to build up the longest common subsequence at the end of
your algorithm.
Optimal Space & Time Complexity
O(nm) time | O(nm) space - where n and m are the lengths of the two input strings.
"""


def longest_common_subsequence(str1, str2):
    longest_common_subsequence = [[[None, 0, None, None] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                longest_common_subsequence[i][j] = [str2[i - 1], longest_common_subsequence[i - 1][j - 1][1] + 1, i - 1,
                                                    j - 1]
            else:
                if longest_common_subsequence[i - 1][j][1] > longest_common_subsequence[i][j - 1][1]:
                    longest_common_subsequence[i][j] = [None, longest_common_subsequence[i - 1][j][1], i - 1, j]
                else:
                    longest_common_subsequence[i][j] = [None, longest_common_subsequence[i][j - 1][1], i, j - 1]
    return build_sequence(longest_common_subsequence)


def build_sequence(lcs):
    sequence = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    while i != 0 and j != 0:
        current_entry = lcs[i][j]
        if current_entry[0] is not None:
            sequence.append(current_entry[0])
        i = current_entry[2]
        j = current_entry[3]
    return list(reversed(sequence))


def main():
    str1 = "ZXVVYZW"
    str2 = "XKYKZPW"
    print(longest_common_subsequence(str1, str2))


if __name__ == "__main__":
    main()
