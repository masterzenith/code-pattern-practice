"""
Given an integer array nums and an integer k, there is a sliding window of size k which is moving from the very left
of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right
by one position, return the median of the current window. Answers within 10^-5 of the actual value will be accepted.

I/P: k = 4
    [1, 3, -1, 2, -2, -3, 5, 1, 5, 3]

O/P: [1.5, 0.5, -1.5, 0.0, -0.5, 3.0, 4.0]

Time: O(nlogn). Need O(nlogn) for sorting.
Space: O(n)
"""


def median_sliding_window(nums, k):
    arr = []
    i = j = 0
    ans = []
    while j < len(nums):
        arr.append(nums[j])
        if j < k - 1:
            j += 1
        elif j - i + 1 == k:
            array = sorted(arr)
            value = 0
            if k % 2 == 0:
                m = k // 2
                value = (array[m - 1] + array[m]) / 2
            else:
                value = array[k // 2]
            ans.append(value)
            if nums[i] in arr:
                arr.pop(0)
            i += 1
            j += 1
    return ans


def main():
    print(median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(median_sliding_window([3, 4, 5, 1, 8, -3, 5, -4], 4))
    print(median_sliding_window([1, 2], 1))


if __name__ == "__main__":
    main()
