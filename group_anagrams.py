from collections import defaultdict


# O(m * n * nlogn) time | O(n)
def group_anagrams(strs):
    # mapping character count to list of Anagrams
    result = defaultdict(list)
    strs.sort()
    for s in strs:
        count = [0] * 26  # a....z
        for c in s:
            count[ord(c) - ord("a")] += 1  # ASCII value of a to find out poisiton 0 of a
        result[tuple(count)].append(s)
    return result.values()


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
