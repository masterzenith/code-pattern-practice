"""
Group Anagrams
Write a function that takes in an array of strings and groups anagrams together.
Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and "iceman"
are anagrams; similarly, "foo" and "ofo" are anagrams.
Your function should return a list of anagram groups in no particular order.
Sample Input:
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
Sample Output:
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

Hints:
1. Try rearranging every input string such that each string's letters are ordered in alphabetical order. What can you do
with the resulting strings?
2. For any two of the resulting strings mentioned in Hint #1 that are equal to each other, their original strings (with
their letters in normal order) must be anagrams. Realizing this, you could bucket all of these resulting strings together,
all the while keeping track of their original strings, to find the groups of anagrams.
3. Can you simply store the resulting strings mentioned in Hint #1 in a hash table and find the groups of anagrams using
this hash table?

Optimal Space & Time Complexity
O(w * n * log(n)) time | O(wn) space - where w is the number of words and n is the length of the longest word
"""


def group_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())


def main():
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    print(group_anagrams(words))


if __name__ == "__main__":
    main()