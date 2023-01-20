"""
Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater
than a given 'key'.
Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first
letter. This also means that the smallest letter in the given array is greater than the last letter of the array and is
also the first letter of the array.

Write a function to return the next letter of the given 'key'

I/P: ['a', 'c', 'f', 'h'], key = 'f'
O/P: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.

I/P: ['a', 'c', 'f', 'h'], key = 'b'
O/P: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.

Time: O(logN) where 'N' is the total elements in the given array. We are reducing the search range by half at every step.
Space: The algorithm runs in constant space O(1)
"""


def search_next_letter(letters, key):
    n = len(letters)
    # The array is considered circular, which means if the 'key' is bigger than the last letter of the array or if it
    # is smaller than the first letter of the array, the key's next letter will be the first letter of the array.
    if key < letters[0] or key > letters[n - 1]:
        return letters[0]
    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
    # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end + 1'
    return letters[start % n]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


if __name__ == "__main__":
    main()
