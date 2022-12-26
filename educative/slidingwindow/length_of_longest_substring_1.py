"""
Given an array containing 0s and 1s, if you are allowed to replace no more than 'k' 0s with 1s, find the length of the
longest contiguous subarray having all 1s.
I/P: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
O/P: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

I/P: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
O/P: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

Time: O(N) where N is the count of numbers in the input array.
Space: The algorithm runs in constant space O(1).
"""


def length_of_longest_substring_1(arr, k):
    window_start, max_length, max_ones_count = 0, 0, 0

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        # Current window size is from window_start to window_end, overall we have a maximum of 1s repeating
        # 'max_ones_count' times, this means we can have a window with 'max_ones_count' 1s and the remaining are 0s
        # which should replace with 1s. Now, if the remaining 0s are more than 'k', it is the time to shrink the window
        # as we aren't allowed to replace more than 'k' 0s
        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring_1([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring_1([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


if __name__ == "__main__":
    main()
