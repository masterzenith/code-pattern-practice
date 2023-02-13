"""
Knuth—Morris—Pratt Algorithm
Write a function that takes in two strings and checks if the first string contains the second one using the Knuth—Morris—Pratt algorithm.
The function should return a boolean.
If you're unfamiliar with the Knuth—Morris—Pratt Algorithm, we recommend watching the Conceptual Overview section of this
question's video explanation before starting to code.
Sample Input:
string = "aefoaefcdaefcdaed"
substring = "aefcdaed"
Sample Output:
true

Hints:
1. The Knuth—Morris—Pratt algorithm works by identifying patterns in the potential substring and exploiting them to avoid
doing needless character comparisons when searching for the substring in the main string. For instance, take the string
"ababac" and the substring "abac"; comparing these strings will fail at the fourth character, where "b" is not equal to "c".
Instead of having to restart our comparisons at the second character of the main string, however, we notice that the
substring "ab", which is at the beginning of our potential substring, just appeared near our point of failure in the main
string. How can we use this to our advantage?
2. Start by traversing the potential substring and building out a pattern table. This 1-dimensional array should store,
for every position in the substring, the last index at which a matching pattern has been seen; more specifically, this
index should be the ending index of a prefix in the substring that is also a suffix at the given position. For example,
the string "abcababcd" should yield the following pattern table: [-1, -1, -1, 0, 1, 0, 1, 2, -1].
3. After the pattern table mentioned in Hint #2 has been built, traverse the main string and the potential substring with
two separate pointers. When characters match, move the pointers forward. When characters don't match, check if the pointer
in the substring is at the very beginning of the substring; if it is, then there is no match and you can move the pointer
of the main string forward until there is a match; if it isn't, then move it to the position that comes right after the last
seen pattern stored at the previous index in the pattern table.

Optimal Space & Time Complexity
O(n + m) time | O(m) space - where n is the length of the main string and m is the length of the potential substring

~~~
** The time complexity of the Knuth-Morris-Pratt algorithm is O(n), where n is the length of the text. This is because the
algorithm scans the text exactly once and performs a constant amount of work for each character.
** The space complexity of the algorithm is O(m), where m is the length of the pattern. This is because the algorithm uses
a lps array of size m to store the computed longest proper prefix-suffix values for the pattern.

Note that the time and space complexity of the computeLPSArray function is also O(m).
~~~
"""


def KMP_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0] * m
    j = 0
    compute_LPS_Array(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return True
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


def compute_LPS_Array(pattern, m, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


def main():
    string = "aefoaefcdaefcdaed"
    substring = "aefcdaed"
    print(KMP_search(string, substring))


if __name__ == "__main__":
    main()
