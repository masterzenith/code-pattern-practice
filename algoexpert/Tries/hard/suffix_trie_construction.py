"""
Special Strings
Write a function that takes in a list of non-empty strings and returns a list of all the special strings found in the
input list.
A string is said to be special if it's exactly made up of at least two instances of other strings in the input list of
strings.
In order for a string to be special, just containing two instances of other strings isn't sufficient; the string must be
exactly made up of those other strings. For example, in the list ["a", "b", "abc"], the string "abc" isn't special, even
though it contains "a" and "b", because "c" isn't a string in the list.
Note that strings can be repeated to form a special string; for instance, in the list ["a", "aaa"], the string "aaa" is
a special string because it's made up of three repeated instances of "a".
Also note that you can't use language-built-in string-matching methods.

Sample Input:
strings = [
  "foobarbaz",
  "foo",
  "bar",
  "foobarfoo",
  "baz",
  "foobaz",
  "foofoofoo",
  "foobazar",
]
Sample Output:
["foobarbaz", "foobarfoo", "foobaz", "foofoofoo"]

Time and Space Complexity:
Average case: when there aren't too many strings with identical prefixes that are found in another string
O(n * m) time | O(n * m) space - where n is the number of strings and m is the length of the longest string
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.end_symbol = "*"

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.children[self.end_symbol] = TrieNode()


def is_special(word, node, idx, count, trie):
    char = word[idx]
    if char not in node.children:
        return False
    next_node = node.children[char]
    at_end_of_string = idx == len(word) - 1
    if trie.end_symbol in next_node.children:
        is_complete = next_node.children[trie.end_symbol].is_end
        if at_end_of_string:
            return is_complete and count + 1 >= 2
        if is_complete:
            rest_is_special = is_special(word, trie.root, idx + 1, count + 1, trie)
            if rest_is_special:
                return True
    return is_special(word, next_node, idx + 1, count, trie)


def special_strings(strings):
    trie = Trie()
    for word in strings:
        trie.insert(word)
    output = []
    for word in strings:
        if is_special(word, trie.root, 0, 0, trie):
            output.append(word)
    return output


def main():
    strings = [
        "foobarbaz",
        "foo",
        "bar",
        "foobarfoo",
        "baz",
        "foobaz",
        "foofoofoo",
        "foobazar",
    ]
    print(special_strings(strings))


if __name__ == "__main__":
    main()
