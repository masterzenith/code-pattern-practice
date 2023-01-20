"""
Develop a program for making automatic investment decisions for a busy investor. The investor has some start-up capital,
c to invest and a portfolio of projects in which they would like to invest in. The investor wants to maximize their
cumulative capital as a result of this investment.

I/P: k = 3, c = 2
Capitals: [1, 2, 3, 4]
Profits: [1, 3, 5, 7]
--------------------------
Selected capitals = 2, 4, 3
Selected Profits = 3, 7, 5
Maximum Capital = 2 + 3 + 7 + 5 = 17

O/P: Maximum capital = 17

Time: O(NlogN). Sorting the projects by increasing capital takes O(nlogn) time. Also, we perform O(n) operations with
    the priority queue, each in O(logn)
Space: O(n). The sorted array of projects and the priority queue take linear space.
"""
from heapq import *


class min_heap:
    def __init__(self):
        self.min_heap_list = []

    def insert(self, x):
        heappush(self.min_heap_list, x)

    def get_min(self):
        return self.min_heap_list[0]

    def __str__(self):
        out = "["
        for i in self.min_heap_list:
            out += str(i) + ", "
        out = out[:-2] + "]"
        return out


class max_heap:
    def __init__(self):
        self.max_heap_list = []

    def insert(self, x):
        heappush(self.max_heap_list, x)

    def get_max(self):
        return -self.max_heap_list[0]

    def __str__(self):
        out = "["
        for i in self.max_heap_list:
            out += str(i) + ", "
        out = out[:-2] + "]"
        return out


def maximum_capital(k, w, profits, capitals):
    n = len(profits)
    projects = list(zip(capitals, profits))
    projects.sort()
    # heapq is a min heap, but we need a max heap
    # so we will store negated elements
    q = []
    ptr = 0
    for i in range(k):
        while ptr < n and projects[ptr][0] <= w:
            # push a negated element
            heappush(q, -projects[ptr][1])
            ptr += 1
        if not q:
            break
        # pop a negated element
        w += -heappop(q)

    return w


def main():
    print(maximum_capital(1, 2, [1, 2, 2, 3], [2, 4, 6, 8]))
    print(maximum_capital(2, 2, [1, 2, 3, 4], [1, 3, 5, 7]))
    print(maximum_capital(2, 3, [1, 3, 4, 5, 6], [1, 2, 3, 4, 5]))
    print(maximum_capital(3, 0, [1, 2, 3], [0, 1, 2]))


if __name__ == "__main__":
    main()
