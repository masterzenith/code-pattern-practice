"""
Implement a data structure that'll store a dynamically growing list of integers and provide access to their median in
O(1).
I/P: Stream: [22, 35, 30]
O/P: median = 30.0
"""


class MedianFinder:
    def __init__(self):
        # two heaps, large: minheap, small: maxheap
        # heaps should be equal size
        self.small, self.large = [], []

    def find_median(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


def main():
    median_finder = MedianFinder()
    print(median_finder.find_median([22, 35, 30]))


if __name__ == "__main__":
    main()
