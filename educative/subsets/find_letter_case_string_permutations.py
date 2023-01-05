"""
Given a string, find all of its permutations preserving the character sequence but changing case.
I/P: "ad52"
O/P: "ad52", "Ad52", "aD52", "AD52"

Time: Since we have 2^N permutations at the most and while processing each permutation we convert it into a character
    array, the overall time complexity of the algo will be O(N*2^N)
Space: All the additional space used by our algorithm is for the output list. Since we can have a total of O(2^N)
        permutations, the space complexity of this algo is O(N*2^N)

"""


def find_letter_case_string_permutations(str1):
    permutations = [str1]
    # process every character of the string one by one
    for i in range(len(str1)):
        if str1[i].isalpha():   # only process characters, skip digits
            # we will take all existing permutations and change the letter case appropriately
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                # if the current character is in upper case, change it to lower case or vice versa
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))
    return permutations


def main():
    print("String permutations are: " + str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " + str(find_letter_case_string_permutations("ab7c")))


if __name__ == "__main__":
    main()
