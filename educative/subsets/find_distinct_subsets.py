"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.
Example 1:
I/P: [1, 3, 3]
O/P: [], [1], [3], [1, 3], [3, 3], [1, 3, 3]

Time: O(N*2^N)
Space: O(N*2^N)
"""


def find_distinct_subsets(nums):
    # sort the numbers to handle duplicates
    list.sort(nums)
    subsets = []
    subsets.append([])
    start_idx, end_idx = 0, 0
    for i in range(len(nums)):
        start_idx = 0
        # if current and the previous elements are same, create new subsets only from the subsets
        # added in the previous step
        if i > 0 and nums[i] == nums[i - 1]:
            start_idx = end_idx + 1
        end_idx = len(subsets) - 1
        for j in range(start_idx, end_idx + 1):
            # create a new subset from the existing subset and add the current element to it
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_distinct_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_distinct_subsets([1, 5, 3, 3])))


if __name__ == "__main__":
    main()
