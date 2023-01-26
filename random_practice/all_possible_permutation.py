def toString(List):
    return ''.join(List)


def all_possible_permutation(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            all_possible_permutation(a, l + 1, r)
            # backtrack
            a[l], a[i] = a[i], a[l]


string = "ABC"
n = len(string)
a = list(string)
all_possible_permutation(a, 0, n - 1)
