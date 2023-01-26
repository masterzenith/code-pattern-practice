# Indeed karat interview question

user0 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user2 = ["a", "/one", "/two"]
user3 = ["/red", "/orange", "/yellow", "/green", "/blue", "/purple", "/white", "/amber", "/HotRodPink",
         "/BritishRacingGreen"]
user4 = ["/red", "/orange", "/amber", "/random", "/green", "/blue", "/purple", "/white", "/lavender", "/HotRodPink",
         "/BritishRacingGreen"]
user5 = ["a"]


def best_range(nums):
    maxrun = -1
    rl = {}
    for x in nums:
        run = rl[x] = rl.get(x - 1, 0) + 1
        if run > maxrun:
            maxend, maxrun = x, run
    return (maxend - maxrun + 1, maxend)


# O(n) < Time Complexity
# O(n) < Space Complxity
def findContiguousHistory(u1, u2):
    set_history_u1 = set(u1)
    set_history_u2 = set(u2)

    both_history = set_history_u1 & set_history_u2

    if len(both_history) > 0:
        # print(both_history)
        u1_positions = [u1.index(x) for x in u1 if x in both_history]
        u2_positions = [u2.index(x) for x in u1 if x in both_history]

        print(u1_positions)
        print(u2_positions)

        contiguous_u1 = best_range(u1_positions)
        contiguous_u2 = best_range(u2_positions)

        print(contiguous_u1)
        print(contiguous_u2)

        contiguous_u1_count = contiguous_u1[1] - contiguous_u1[0] + 1
        contiguous_u2_count = contiguous_u2[1] - contiguous_u2[0] + 1

        # print(contiguous_u1_count)
        # print(contiguous_u2_count)

        max_contiguous = min([contiguous_u1_count, contiguous_u2_count])

        # print(max_contiguous)

        if len(contiguous_u1) == max_contiguous:
            return u1[contiguous_u1[0]:contiguous_u1[1] + 1]
        else:
            return u2[contiguous_u2[0]:contiguous_u2[1] + 1]
    else:
        return []


print(findContiguousHistory(user0, user1))
