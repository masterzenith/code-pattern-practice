"""
Subarray Sort:
Write a function that takes in an array of at least two integers and that returns an array of the starting and ending
indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array
to be sorted (in ascending order).
If the input array is already sorted, the function should return [-1, -1].
Sample Input:
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Sample Output:
[3, 9]

Hints:
1. Realize that even a single out-of-order number in the input array can call for a large subarray to have to be sorted.
This is because, depending on how out-of-place the number is, it might need to be moved very far away from its original
position in order to be in its sorted position.
2. Find the smallest and largest numbers that are out of order in the input array. You should be able to do this in a
single pass through the array.
3. Once you've found the smallest and largest out-of-order numbers mentioned in Hint #2, find their final sorted
positions in the array. This should give you the extremities of the smallest subarray that needs to be sorted.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the input array
"""


def subarray_sort(array):
    min_out_of_order = float("inf")
    max_out_of_order = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if is_out_of_order(i, num, array):
            min_out_of_order = min(min_out_of_order, num)
            max_out_of_order = max(max_out_of_order, num)
    if min_out_of_order == float("inf"):
        return [-1, -1]
    sub_array_left_idx = 0
    while min_out_of_order >= array[sub_array_left_idx]:
        sub_array_left_idx += 1
    sub_array_right_idx = len(array) - 1
    while max_out_of_order <= array[sub_array_right_idx]:
        sub_array_right_idx -= 1
    return [sub_array_left_idx, sub_array_right_idx]


def is_out_of_order(i, num, array):
    if i == 0:
        return num > array[i+1]
    if i == len(array) - 1:
        return num < array[i-1]
    return num > array[i+1] or num < array[i-1]


def main():
    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    print(subarray_sort(array))


if __name__ == "__main__":
    main()
