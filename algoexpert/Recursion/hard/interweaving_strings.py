"""
Interweaving Strings
Write a function that takes in three strings and returns a boolean representing whether the third string can be formed
by interweaving the first two strings.
To interweave strings means to merge them by alternating their letters without any specific pattern. For instance, the
strings "abc" and "123" can be interwoven as "a1b2c3", as "abc123", and as "ab1c23" (this list is nonexhaustive).
Letters within a string must maintain their relative ordering in the interwoven string.

Sample Input:
one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"

Sample Output:
true

Hints:
1. Try traversing the three strings with three different pointers to solve this problem.
2. Declare three variables (i, j, and k, for instance) pointing to indices in the three strings, respectively, and
starting at 0. At any given combination of indices, if neither the character at i in the first string nor the character
at j in the second string is equal to the character at k in the third string, then the first two strings can't interweave
to form the third one (at least not in whatever way led to the values of i, j, and k in question).
3. If at any given combination of the indices i, j, and k mentioned in Hint #2, the character at i in the first string
or the character at j in the second string is equal to the character at k in the third string, then you can potentially
interweave the first two strings to get the third one. In such a case, try incrementing the two relevant indices (i and
k or j and k) and repeating this process until you confirm whether or not the first two strings can be interwoven to form
the third one. Try using recursion to implement this algorithm.
4. By following Hint #3, you'll perform, in some cases, many computations multiple times. How can you use caching to
improve the time complexity of this algorithm?

Optimal Space & Time Complexity
O(nm) time | O(nm) space - where n is the length of the first string and m is the length of the second string

https://github.com/lee-hen/Algoexpert/tree/master/hard/30_interweaving_strings#hints
"""


def can_interweave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False

    # Create a 2D table to keep track of whether s3[0:i+j] can be formed by interweaving s1[0:i] and s2[0:j]
    table = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Base case: an empty s1 and s2 can only interweave to form an empty s3
    table[0][0] = True

    # Check if s1 and s3 match for i = 1 to len(s1)
    for i in range(1, len(s1) + 1):
        if s1[i - 1] == s3[i - 1]:
            table[i][0] = True
        else:
            break

    # Check if s2 and s3 match for j = 1 to len(s2)
    for j in range(1, len(s2) + 1):
        if s2[j - 1] == s3[j - 1]:
            table[0][j] = True
        else:
            break

    # Check if s3[0:i+j] can be formed by interweaving s1[0:i] and s2[0:j]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s3[i + j - 1] and table[i - 1][j]:
                table[i][j] = True
            elif s2[j - 1] == s3[i + j - 1] and table[i][j - 1]:
                table[i][j] = True

    return table[-1][-1]


def main():
    one = "algoexpert"
    two = "your-dream-job"
    three = "your-algodream-expertjob"
    print(can_interweave(one, two, three))


if __name__ == "__main__":
    main()
