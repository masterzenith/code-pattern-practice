"""
Given an array of intervals representing N appointments, find out if a person can attend all the appointments.
E1:
Appointments: [[1, 4], [2, 5], [7, 9]]
Output: false
Explanation: Since [1, 4] and [2, 5] overlap, a person cannot attend both of these appointments.

E2:
Appointments: [[6, 7], [2, 4], [8, 12]]
Output: true
Explanation: None of the appointments overlap, a person can attend all of these appointments.

E3:
Appointments: [[4, 5], [2, 3], [3, 6]]
Output: false
Explanation: Since [4, 5] and [3, 6] overlap, a person cannot attend both of these appointments.

Time: O(N*logN), where N is the total number of appointments. Though we are iterating the intervals only once,
    Our algo will take O(N*logN) since we need to sort them in the beginning.
Space: O(N), which we need for sorting. For java, Arrays.sort() uses Timsort, which needs O(N) space

Similar Problem:
Given a list of appointments, find all the conflicting appointments
Example:
    Appointments: [[4, 5], [2, 3], [3, 6], [5, 7], [7, 8]]
    Output: [4, 5] and [3, 6] conflict
            [3, 6] and [5, 7] conflict 
"""


def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    start, end = 0, 1
    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i-1][end]:
            # Please note the comparison above, it is "<" and not "<="
            # while merging we needed "<=" comparison, as we will be merging the two
            # intervals having condition "intervals[i][start] == intervals[i-1][end]" but
            # such intervals don't represent conflicting appointments as one starts right after the other
            return False
    return True


def main():
    print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


if __name__ == "__main__":
    main()
