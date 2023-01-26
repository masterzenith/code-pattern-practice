def map(l, f):
    return map_acc(l, f, [])


def map_acc(l, f, a):
    if l == []:
        return a
    else:
        b = a + [f(l[0])]
        return map_acc(l[1:], f, b)