"""
Count Contained Permutations
You're given two non-empty strings: a big string and a small string. Write a function that returns the number of
permutations of the small string that are contained in the big string.
Repeated permutations should be counted, and the small string counts as a permutation of itself.

Sample Input:
bigString = "cbabcacabca"
smallString = "abc"
Sample Output:
6 // "cba", "abc", "bca", "cab", "abc", "bca"

Time and Space:
The time complexity of this solution is O(n + m), where n is the length of the big string and m is the length of the small string.
The reason for this time complexity is that the function uses two pointers (left and right) to define the current window
in the big string, and each character in the big string is processed only once. When the right pointer moves, the character
count in big_count is incremented and the number of characters in the small string that have been seen in the current window
is updated if necessary. When the count variable equals the length of the small string, the left pointer is moved until
the count is no longer equal to the length of the small string, and the process repeats. This ensures that each character
in the big string is processed only once, giving a time complexity of O(n).

The space complexity of this solution is O(m), where m is the length of the small string. This is because the function
uses two dictionaries small_count and big_count to store the count of each character in the small string and the count
of characters seen in the current window in the big string, respectively. The size of these dictionaries is directly
proportional to the size of the small string, so the space complexity is O(m).
"""


def permutations_in_string(big, small):
    from collections import Counter

    n, m = len(big), len(small)
    small_count = Counter(small)
    big_count = Counter()

    left, right, count = 0, 0, 0
    result = 0
    while right < n:
        big_count[big[right]] += 1
        if big_count[big[right]] <= small_count[big[right]]:
            count += 1
        right += 1
        while count == m:
            if right - left == m:
                result += 1
            big_count[big[left]] -= 1
            if big_count[big[left]] < small_count[big[left]]:
                count -= 1
            left += 1
    return result


def main():
    bigString = "cbabcacabca"
    smallString = "abc"
    print(permutations_in_string(bigString, smallString))


if __name__ == "__main__":
    main()
