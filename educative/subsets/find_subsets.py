"""
Given a set with distinct elements, find all of its distinct subsets.
I/P: [1, 3]
O/P: [], [1], [3], [1, 3]

I/P: [1, 5, 3]
O/P: [], [1], [5], [3], [1, 5], [1, 3], [5, 3], [1, 5, 3]

Time: Since, in each step, the number of subsets doubles as we add each element to all existing subsets, therefore
        we will have a total of O(2^N) subsets where N is the total number of elements in the input set. And since we
        construct a new subset from an existing set, therefore the time complexity of the algo is O(N*2^N).
Space: O(N*2^N)
"""


def find_subsets(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])
    for current_number in nums:
        # we will take all existing subsets and insert the current number in them to create new subsets
        n = len(subsets)
        for i in range(n):
            # create a new subset from the existing subset and insert the current element to it
            set1 = list(subsets[i])
            set1.append(current_number)
            subsets.append(set1)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


if __name__ == "__main__":
    main()
