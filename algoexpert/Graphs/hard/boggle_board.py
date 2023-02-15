"""
Boggle Board
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing letters; this matrix
represents a boggle board. You're also given a list of words.
Write a function that returns an array of all the words contained in the boggle board. The final words don't need to be
in any particular order.
A word is constructed in the boggle board by connecting adjacent (horizontally, vertically, or diagonally) letters,
without using any single letter at a given position more than once; while a word can of course have repeated letters,
those repeated letters must come from different positions in the boggle board in order for the word to be contained in
the board. Note that two or more words are allowed to overlap and use the same letters in the boggle board.

Sample Input:
board = [
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"],
],
words = [
    "this", "is", "not", "a", "simple", "boggle",
    "board", "test", "REPEATED", "NOTRE-PEATED",
]

Sample Output:
["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
// The words could be ordered differently.

Hints:
1. You can divide this question into two separate problems: one part involves traversing the boggle board in such a way
that allows you to construct strings letter by letter; the other part involves actually comparing the strings you construct
in the board against the words in the list that you're given. For the second part, what data structure lends itself very
well to matching characters to multiple strings at once?
2. Try creating a trie out of the input list of words. This will allow you to compare letters in the boggle board against
all input words in constant time. How can you efficiently traverse the boggle board to construct all potentially valid
strings, without counting letters twice in any string?
3. Treat the board as a graph, where each element in the board is a node with up to 8 neighboring nodes. Traverse it in
a depth-first-search-like fashion, checking if letters are contained in the trie and traversing the trie simultaneously
 if it makes sense to do so. How can you keep track of letters that you've already visited in order to avoid erroneously
 counting some of them twice in a single string? Could you keep track of visited nodes in an auxiliary data structure?
4. Keeping in mind that you only want to mark nodes as visited in a single branch of the graph that you're traversing
(i.e., you don't want the state of visited nodes in one branch of the graph to spill into the state of another branch of
the graph), try marking any node you traverse as unvisited at the end of the recursive call that actually traverses it,
after traversing through all the node's neighbors and performing the same actions on them recursively.

Optimal Space & Time Complexity
O(nm*8^s + ws) time | O(nm + ws) space - where n is the width the board, m is the height of the board, w is the number
of words, and s is the length of the longest word

Other Solutions:
https://github.com/das-jishu/algoexpert-data-structures-algorithms/blob/master/Hard/boggle-board.py
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_word = True

    def search(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                return None
            current = current.children[c]
        return current


def find_words(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    def dfs(i, j, node, path, visited, words_found):
        if node.is_word:
            words_found.add(path)

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return

        if (i, j) in visited:
            return

        c = board[i][j]
        child_node = trie.search(c)
        if not child_node:
            return

        visited.add((i, j))
        for ni, nj in (
        (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)):
            dfs(ni, nj, child_node, path + c, visited, words_found)
        visited.remove((i, j))

    words_found = set()
    visited = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            c = board[i][j]
            node = trie.search(c)
            if not node:
                continue
            dfs(i, j, node, c, visited, words_found)

    return list(words_found)


def main():
    board = [
                ["t", "h", "i", "s", "i", "s", "a"],
                ["s", "i", "m", "p", "l", "e", "x"],
                ["b", "x", "x", "x", "x", "e", "b"],
                ["x", "o", "g", "g", "l", "x", "o"],
                ["x", "x", "x", "D", "T", "r", "a"],
                ["R", "E", "P", "E", "A", "d", "x"],
                ["x", "x", "x", "x", "x", "x", "x"],
                ["N", "O", "T", "R", "E", "-", "P"],
                ["x", "x", "D", "E", "T", "A", "E"],
            ]

    words = [
        "this", "is", "not", "a", "simple", "boggle",
        "board", "test", "REPEATED", "NOTRE-PEATED",
    ]
    print(find_words(board, words))


if __name__ == "__main__":
    main()
