"""
Multi String Search
Write a function that takes in a big string and an array of small strings, all of which are smaller in length than the
big string. The function should return an array of booleans, where each boolean represents whether the small string at
that index in the array of small strings is contained in the big string.
Note that you can't use language-built-in string-matching methods.
Sample Input #1:
bigString = "this is a big string"
smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
Sample Output #1:
[true, false, true, true, false, true, false]

Sample Input #2:
bigString = "abcdefghijklmnopqrstuvwxyz"
smallStrings = ["abc", "mnopqr", "wyz", "no", "e", "tuuv"]
Sample Output #2:
[true, true, false, true, true, false]

Hints:
1. A simple way to solve this problem is to iterate through all the small strings, checking if each of them is
contained in the big string by iterating through the big string's characters and comparing them to the given small
string's characters with a couple of loops. Is this approach efficient from a time-complexity point of view?
2. Try building a suffix-trie-like data structure containing all the big string's suffixes. Then, iterate through
all the small strings and check if each of them is contained in the data structure you've created. What are the
time-complexity ramifications of this approach?
3. Try building a trie containing all the small strings. Then, iterate through the big string's characters and check
if any part of the big string is a string contained in the trie you've created. Is this approach better than the one
described in Hint #2 from a time-complexity point of view?

Optimal Space & Time Complexity
O(ns + bs) time | O(ns) space - where n is the number of small strings, s is the length of longest small string, and b
is the length of the big string

Other Solution:
https://github.com/das-jishu/algoexpert-data-structures-algorithms/blob/master/Hard/multi-string-search.py
"""


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def insert(self, string):
        current = self.root
        for i in range(len(string)):
            if string[i] not in current:
                current[string[i]] = {}
            current = current[string[i]]
        current[self.end_symbol] = string


def multi_string_search(big_string, small_strings):
    trie = Trie()
    for string in small_strings:
        trie.insert(string)
    contained_strings = {}
    for i in range(len(big_string)):
        find_small_strings_in(big_string, i, trie, contained_strings)
    return [string in contained_strings for string in small_strings]


def find_small_strings_in(string, start_idx, trie, contained_strings):
    current_node = trie.root
    for i in range(start_idx, len(string)):
        current_char = string[i]
        if current_char not in current_node:
            break
        current_node = current_node[current_char]
        if trie.end_symbol in current_node:
            contained_strings[current_node[trie.end_symbol]] = True


def main():
    bigString = "this is a big string"
    smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
    print(multi_string_search(bigString, smallStrings))


if __name__ == "__main__":
    main()

