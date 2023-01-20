"""
Given an infinite sorted array(or an array with unknown size), find if a given number 'key' is present in the array.
Write a function to return the index of the 'key' if it is present in the array, otherwise return -1.
Since it is not possible to define an array with infinite(unknown) size, you will be provided with an interface
ArrayReader to read elements of the array. ArrayReader.get(index) will return the number at index; if the array's size
is smaller than the index it will return Integer.MAX_VALUE

I/P: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
O/P: 6
Explanation: The key is present at index '6' in the array

I/P: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
O/P: -1
Explanation: The key is not present in the array.

Time: There are two parts of this algo. In the first part, we keep increasing the bound's size exponentially
    (double it every time) while searching for the proper bounds. Therefore, this step will take O(logN) assuming that
    the array will have maximum 'N' numbers. In the second step, we perform the binary search which will take O(logN),
    so the overall time complexity of this algo will be O(logN)

Space: The algo runs in constant space O(1).
"""
import math


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    # find the proper bounds first
    start, end = 0, 1
    while reader.get(end) < key:
        new_start = end + 1
        end += (end - start + 1) * 2
        # increase to double the bounds size
        start = new_start
    return binary_search(reader, start, end, key)


def binary_search(reader, start, end, key):
    while start <= end:
        mid = start + (end - start) // 2
        if key < reader.get(mid):
            end = mid - 1
        elif key > reader.get(mid):
            start = mid + 1
        else:   # found the key
            return mid
    return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


if __name__ == "__main__":
    main()
