"""
Longest Streak Of Adjacent Ones:
Write a function that takes in a non-empty array of only 0s and 1s and returns the index of the 0 that, if replaced by
a 1, would form the longest streak of adjacent 1s in the entire array.
If there are no 0s in the array, your function should return -1; if there are multiple possible answers, your function
can return any of them.

Sample Input:
  array = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1]
Sample Output:
      8 // Replacing the 0 at index 8 with a 1 forms a streak of 6 adjacent 1s.


Time and Space:
O(n) time | O(1) space - where n is the length of the input array
"""


def longest_streak(arr):
    max_len = 0
    max_index = -1
    curr_len = 0
    for i, num in enumerate(arr):
        if num == 1:
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
                max_index = i - curr_len
            curr_len = 0
    if curr_len > max_len:
        max_index = len(arr) - curr_len
    return max_index if max_index != -1 else -1


def main():
    array = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1]
    print(longest_streak(array))


if __name__ == "__main__":
    main()
