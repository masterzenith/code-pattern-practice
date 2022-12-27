"""
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted
on their start time.

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists

Time: O(N +M) where N and M are the total number of intervals in the input arrays respectively
Space: Ignoring the space needed for the result list, the algo runs in constant space O(1)
"""


def merge_intersection(intervals_a, intervals_b):
    result = []
    i, j, start, end = 0, 0, 0, 1

    while i < len(intervals_a) and j < len(intervals_b):
        # check if intervals overlap and intervals_a[i]'s start time lies within the other intervals_b[j]
        a_overlaps_b = intervals_b[j][start] <= intervals_a[i][start] <= intervals_b[j][end]

        # check if intervals overlap and intervals_a[j]'s start time lies within the other intervals_b[i]
        b_overlaps_a = intervals_a[i][start] <= intervals_b[j][start] <= intervals_a[i][end]

        # store the intersection part
        if a_overlaps_b or b_overlaps_a:
            result.append([max(intervals_a[i][start], intervals_b[j][start]),
                           min(intervals_a[i][end], intervals_b[j][end])])

        # move next from the internal which is finishing first
        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1
    return result


def main():
    print("Intervals Intersection: " + str(merge_intersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge_intersection([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


if __name__ == "__main__":
    main()

