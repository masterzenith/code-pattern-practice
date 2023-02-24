"""
Quick Sort
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Quick Sort
algorithm to sort the array.
If you're unfamiliar with Quick Sort, we recommend watching the Conceptual Overview section of this question's video
explanation before starting to code.

Sample Input:
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output:
[2, 3, 5, 5, 6, 8, 9]

Hints:
1. Quick Sort works by picking a "pivot" number from an array, positioning every other number in the array in sorted
order with respect to the pivot (all smaller numbers to the pivot's left; all bigger numbers to the pivot's right), and
then repeating the same two steps on both sides of the pivot until the entire array is sorted.
2. Pick a random number from the input array (the first number, for instance) and let that number be the pivot. Iterate
through the rest of the array using two pointers, one starting at the left extremity of the array and progressively moving
to the right, and the other one starting at the right extremity of the array and progressively moving to the left. As you
iterate through the array, compare the left and right pointer numbers to the pivot. If the left number is greater than
the pivot and the right number is less than the pivot, swap them; this will effectively sort these numbers with respect
to the pivot at the end of the iteration. If the left number is ever less than or equal to the pivot, increment the left
pointer; similarly, if the right number is ever greater than or equal to the pivot, decrement the right pointer. Do this
until the pointers pass each other, at which point swapping the pivot with the right number should position the pivot in
its final, sorted position, where every number to its left is smaller and every number to its right is greater.
3. Repeat the process mentioned in Hint #2 on the respective sub-arrays located to the left and right of your pivot, and
keep on repeating the process thereafter until the input array is fully sorted.

Optimal Space & Time Complexity
Best: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array Average: O(nlog(n)) time | O(log(n))
space - where n is the length of the input array Worst: O(n^2) time | O(log(n)) space - where n is the length of the input
array

https://github.com/das-jishu/algoexpert-data-structures-algorithms/blob/master/Hard/quick-sort.py
"""


def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array


def quick_sort_helper(array, low, high):
    # print("QuickSortHelper")
    if low >= high:
        return
    pivot = array[low]
    left = low + 1
    right = high
    while right >= left:
        if array[left] > pivot > array[right]:
            swap(array, left, right)
        if array[left] <= pivot:
            left += 1
        if array[right] >= pivot:
            right -= 1
    swap(array, low, right)
    left_sub_array_is_smaller = right - 1 - low < high - (right + 1)
    if left_sub_array_is_smaller:
        quick_sort_helper(array, low, right - 1)
        quick_sort_helper(array, right + 1, high)
    else:
        quick_sort_helper(array, right + 1, high)
        quick_sort_helper(array, low, right - 1)


def swap(array, one, two):
    array[one], array[two] = array[two], array[one]


def main():
    array = [8, 5, 2, 9, 5, 6, 3]
    print(quick_sort(array))


if __name__ == "__main__":
    main()


