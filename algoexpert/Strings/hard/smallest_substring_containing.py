"""
https://github.com/lee-hen/Algoexpert/tree/master/very_hard/33_smallest_substring_containing

Smallest Substring Containing
You are given two non-empty strings: a big string and a small string. Write a function that returns the smallest substring
in the big string that contains all the small string's characters.
Note that:
The substring can contain other characters not found in the small string. The characters in the substring don't have to
be in the same order as they appear in the small string. If the small string has duplicate characters, the substring has
to contain those duplicate characters (it can also contain more, but not fewer). You can assume that there will only be
one relevant smallest substring.

Sample Input
bigString = "abcd$ef$axb$c$"
smallString = "$$abf"
Sample Output
"f$axb$"

Hints:
1. Try storing all the small string's character counts in a hash table where each character maps to the number of times
that it appears in the small string.
2. Try using two pointers (a left pointer and a right pointer) to traverse through the big string. How can this help you
find the relevant smallest substring?
3. With the two pointers mentioned in Hint #2, move the right pointer to the right in the big string, keeping track of
all the characters you visit in a hash table identical to the one mentioned in Hint #1, until you've found all the
characters contained in the small string. At that point, move the left pointer to the right in the big string, keeping
track of all the characters you "lose", and stop once you no longer have all of the small string's characters in between
the left and right pointers. Then, repeat the process by moving the right pointer forward and implementing the same logic
described in this Hint.
Optimal Space & Time Complexity
O(b + s) time | O(b + s) space - where b is the length of the big input string and s is the length of the small input
string

The time complexity of this algorithm is O(n), where n is the length of the big string. This is because both the start
and end pointers traverse the big string exactly once, so the time it takes to scan through the big string is proportional
to n. The small_dict dictionary takes O(k) time to create, where k is the number of unique characters in the small string,
but this is a constant factor that is independent of the length of the big string. The rest of the operations in the
algorithm take constant time, so the overall time complexity is O(n).
The space complexity of this algorithm is O(k), where k is the number of unique characters in the small string. This is
because the small_dict dictionary stores the count of characters in the small string, and the number of characters in the
small string is proportional to k. The rest of the variables in the algorithm use a constant amount of space, so the
overall space complexity is O(k).
"""


def smallest_substring(big, small):
    small_dict = {}
    for char in small:
        if char not in small_dict:
            small_dict[char] = 1
        else:
            small_dict[char] += 1

    start = 0
    end = 0
    min_len = float("inf")
    min_start = 0
    char_count = 0

    while end < len(big):
        if big[end] in small_dict:
            small_dict[big[end]] -= 1
            if small_dict[big[end]] >= 0:
                char_count += 1

        while char_count == len(small):
            if end - start + 1 < min_len:
                min_len = end - start + 1
                min_start = start
            if big[start] in small_dict:
                small_dict[big[start]] += 1
                if small_dict[big[start]] > 0:
                    char_count -= 1
            start += 1

        end += 1

    return big[min_start:min_start + min_len]


def main():
    bigString = "abcd$ef$axb$c$"
    smallString = "$$abf"
    print(smallest_substring(bigString, smallString))


if __name__ == "__main__":
    main()
