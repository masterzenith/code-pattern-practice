import string


def find_embedded_word(words, s) -> string:
    flag = False
    for word in words:
        for char in word:
            if char in s and word.count(char) <= s.count(char):
                flag = True
            else:
                flag = False
                break
        if flag:
            return word
    return None


def main():
    words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
    string1 = "tcabnihjs"
    string2 = "tbcanihjs"
    string3 = "baykkjl"
    string4 = "bbabylkkj"
    string5 = "ccc"
    string6 = "breadmaking"
    print(find_embedded_word(words, string1))
    print(find_embedded_word(words, string2))
    print(find_embedded_word(words, string3))
    print(find_embedded_word(words, string4))
    print(find_embedded_word(words, string5))
    print(find_embedded_word(words, string6))


main()
