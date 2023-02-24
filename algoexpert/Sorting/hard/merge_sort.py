"""
Merge Sort
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Merge Sort
algorithm to sort the array.
If you're unfamiliar with Merge Sort, we recommend watching the Conceptual Overview section of this question's video
explanation before starting to code.
Sample Input:
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output:
[2, 3, 5, 5, 6, 8, 9]

Hints:
1. Merge Sort works by cutting an array in two halves, respectively sorting those two halves by performing some special
logic, and then merging the two newly-sorted halves into one sorted array. The respective sorting of the two halves is
done by reapplying the Merge Sort algorithm / logic on each half until single-element halves are obtained; these
single-element arrays are sorted by nature and can very easily be merged back together.
2. Divide the input array in two halves by finding the middle-most index in the array and slicing the two halves around
that index. Then, recursively apply Merge Sort to each half, and finally merge them into one single, sorted array by
iterating through their values and progressively adding them to the new array in ascending order.
3. Your implementation of Merge Sort almost certainly uses a lot of auxiliary space and likely does not sort the input
array in place. What is the space complexity of your algorithm? Can you implement a version of the algorithm using only
one additional array of the same length as the input array, and can this version sort the input array in place?

Optimal Space & Time Complexity
Best: O(nlog(n)) time | O(n) space - where n is the length of the input array Average: O(nlog(n)) time | O(n) space -
where n is the length of the input array Worst: O(nlog(n)) time | O(n) space - where n is the length of the input array

https://github.com/das-jishu/algoexpert-data-structures-algorithms/blob/master/Very%20Hard/merge-sort.py
"""


def merge_sort(array):
    if len(array) <= 1:
        return array
    auxiliary = array[:]
    merge_sort_helper(array, 0, len(array) - 1, auxiliary)
    return array


def merge_sort_helper(array, start, end, auxiliary):
    if start == end:
        return
    middle = (start + end) // 2
    merge_sort_helper(auxiliary, start, middle, array)
    merge_sort_helper(auxiliary, middle + 1, end, array)
    merge_two_arrays(array, start, middle, end, auxiliary)


def merge_two_arrays(array, start, middle, end, auxiliary):
    index1 = start
    index2 = middle + 1
    index = start
    while index1 <= middle and index2 <= end:
        if array[index1] < array[index2]:
            auxiliary[index] = array[index1]
            index1 += 1
        else:
            auxiliary[index] = array[index2]
            index2 += 1
        index += 1

    while index1 <= middle:
        auxiliary[index] = array[index1]
        index += 1
        index1 += 1

    while index2 <= end:
        auxiliary[index] = array[index2]
        index += 1
        index2 += 1


def main():
    array = [8, 5, 2, 9, 5, 6, 3]
    print(merge_sort(array))


if __name__ == "__main__":
    main()

