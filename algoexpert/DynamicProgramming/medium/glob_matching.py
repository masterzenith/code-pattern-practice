"""
Glob Matching
In most modern-day computers, glob patterns are used to refer to multiple file names on the computer's system at once.
Glob patterns typically take advantage of the following two special characters:
1. Wildcards, represented by the * symbol, which match any number of characters, including zero characters.
2. Question marks, represented by the ? symbol, which match any single character (exactly one). For example, the glob
pattern "*.js" matches any file name ending in the JavaScript .js extension.

Write a function that takes in a file name and a pattern (both strings) and returns whether that file name matches the pattern.

Sample Input:
fileName = "abcdefg"
pattern = "a*e?g"
Sample Output:
true

~~~
The time complexity of the algorithm can be optimized by using dynamic programming. We can create a 2D table of size
(m + 1) * (n + 1), where m is the length of the file name and n is the length of the pattern. The table is filled such
that dp[i][j] is True if the file name up to the i-th character matches the pattern up to the j-th character. The table
is filled bottom-up, and the final value of dp[m][n] will tell us if the entire file name matches the entire pattern.

The time complexity of this algorithm is O(mn), but it has a lower constant factor compared to the recursive algorithm,
so it's faster in practice. The space complexity of this algorithm is also O(mn).
~~~
"""


def match_pattern(file_name, pattern):
    m = len(file_name)
    n = len(pattern)
    dp = [[False for j in range(n + 1)] for i in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or file_name[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]


def main():
    fileName = "abcdefg"
    pattern = "a*e?g"
    print(match_pattern(fileName, pattern))


if __name__ == "__main__":
    main()
