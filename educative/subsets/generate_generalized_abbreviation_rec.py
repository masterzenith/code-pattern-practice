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


def generate_generalized_abbreviation_rec(word):
    result = []
    generate_generalized_abbreviation_rec_help(word, list(), 0, 0, result)
    return result


def generate_generalized_abbreviation_rec_help(word, ab_word, start, count, result):
    if start == len(word):
        if count != 0:
            ab_word.append(str(count))
        result.append(''.join(ab_word))
    else:
        # continue abbreviating by incrementing the current abbreviation count
        generate_generalized_abbreviation_rec_help(word, list(ab_word), start + 1, count + 1, result)

        # restart abbreviating, append the count and the current character to the string
        if count != 0:
            ab_word.append(str(count))
        new_word = list(ab_word)
        new_word.append(word[start])
        generate_generalized_abbreviation_rec_help(word, new_word, start + 1, 0, result)


def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation_rec("BAT")))

    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation_rec("code")))


if __name__ == "__main__":
    main()