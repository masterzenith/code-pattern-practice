"""
Given a word, write a function to generate all of its unique generalized abbreviations.
Generalized abbreviation of a word can be generated by replacing each substring of the word by the count of characters
in the substring. Take the example of "ab" which has four substrings: "", "a", "b" and "ab". After replacing these
substrings in the actual word by the count of characters we get all the generalized abbreviations: "ab", "1b", "a1" and
"2".

input: "BAT"
O/P: "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"

Time: O(N*2^N)
Space: O(N*2^N)
"""
from collections import deque


class AbbreviatedWord:
    def __init__(self, str, start, count):
        self.str = str
        self.start = start
        self.count = count


def generate_generalized_abbreviation(word):
    word_len = len(word)
    result = []
    queue = deque()
    queue.append(AbbreviatedWord(list(), 0, 0))
    while queue:
        ab_word = queue.popleft()
        if ab_word.start == word_len:
            if ab_word.count != 0:
                ab_word.str.append(str(ab_word.count))
            result.append(''.join(ab_word.str))
        else:
            # continue abbreviating by incrementing the current abbreviation count
            queue.append(AbbreviatedWord(list(ab_word.str), ab_word.start + 1, ab_word.count + 1))

            # restart abbreviating, append the count and the current character to the string
            if ab_word.count != 0:
                ab_word.str.append(str(ab_word.count))

            new_word = list(ab_word.str)
            new_word.append(word[ab_word.start])
            queue.append(AbbreviatedWord(new_word, ab_word.start + 1, 0))
    return result


def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))

    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("code")))


if __name__ == "__main__":
    main()