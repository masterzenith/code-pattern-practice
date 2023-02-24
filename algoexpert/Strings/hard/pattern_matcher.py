"""
Pattern Matcher
You're given two non-empty strings. The first one is a pattern consisting of only "x"s and / or "y"s; the other one is a
normal string of alphanumeric characters. Write a function that checks whether the normal string matches the pattern.
A string S0 is said to match a pattern if replacing all "x"s in the pattern with some non-empty substring S1 of S0 and
replacing all "y"s in the pattern with some non-empty substring S2 of S0 yields the same string S0.
If the input string doesn't match the input pattern, the function should return an empty array; otherwise, it should
return an array holding the strings S1 and S2 that represent "x" and "y" in the normal string, in that order. If the
pattern doesn't contain any "x"s or "y"s, the respective letter should be represented by an empty string in the final
array that you return.
You can assume that there will never be more than one pair of strings S1 and S2 that appropriately represent "x" and "y"
in the normal string.

Sample Input:
pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"
Sample Output:
["go", "powerranger"]

Hints:
1. Start by checking if the pattern starts with an "x". If it doesn't, consider generating a new pattern that swaps all
"x"s for "y"s and vice versa; this might greatly simplify the rest of your algorithm. Make sure to keep track of whether
or not you do this swap, as your final answer will be affected by it.
2. Use a hash table to store the number of "x"s and "y"s that appear in the pattern, and keep track of the position of
the first "y". Knowing how many "x"s and "y"s appear in the pattern, paired with the length of the main string which you
have access to, will allow you to quickly test out various possible lengths for "x" and "y". Knowing where the first "y"
appears in the pattern will allow you to actually generate potential substrings.
3. Traverse the main string and try different combinations of substrings that could represent "x" and "y". For each
potential combination, map the new pattern mentioned in Hint #1 and see if it matches the main string.

Optimal Space & Time Complexity
O(n^2 + m) time | O(n + m) space - where n is the length of the main string and m is the length of the pattern

Image Explanation:
https://github.com/lee-hen/Algoexpert/tree/master/hard/44_pattern_matcher#hints
"""


def pattern_matcher(pattern, string):
    if len(pattern) > len(string):
        return []
    new_pattern = get_new_pattern(pattern)
    did_switch = new_pattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    first_Y_pos = get_counts_and_first_y_pos(new_pattern, counts)
    if counts["y"] != 0:
        for len_of_X in range(1, len(string)):
            len_of_Y = (len(string) - len_of_X * counts["x"]) / counts["y"]
            if len_of_Y <= 0 or len_of_Y % 1 != 0:
                continue
            len_of_Y = int(len_of_Y)
            yidx = first_Y_pos * len_of_X
            x = string[:len_of_X]
            y = string[yidx: yidx + len_of_Y]
            potential_match = map(lambda char: x if char == "x" else y, new_pattern)
            if string == "".join(potential_match):
                return [x, y] if not did_switch else [y, x]
    else:
        len_of_X = len(string) / counts["x"]
        if len_of_X % 1 == 0:
            len_of_X = int(len_of_X)
            x = string[:len_of_X]
            potential_match = map(lambda char: x, new_pattern)
            if string == "".join(potential_match):
                return [x, ""] if not did_switch else ["", x]
    return []


def get_new_pattern(pattern):
    pattern_letters = list(pattern)
    if pattern[0] == "x":
        return pattern_letters
    else:
        return list(map(lambda char: "x" if char == "y" else "y", pattern_letters))


def get_counts_and_first_y_pos(pattern, counts):
    first_Y_pos = None
    for i, char in enumerate(pattern):
        counts[char] += 1
        if char == "y" and first_Y_pos is None:
            first_Y_pos = i
    return first_Y_pos


def main():
    pattern = "xxyxxy"
    string = "gogopowerrangergogopowerranger"
    print(pattern_matcher(pattern, string))


if __name__ == "__main__":
    main()