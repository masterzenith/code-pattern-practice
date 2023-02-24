"""
Lowest Common Manager
You're given three inputs, all of which are instances of an OrgChart class that have a directReports property pointing
to their direct reports. The first input is the top manager in an organizational chart (i.e., the only instance that isn't
anybody else's direct report), and the other two inputs are reports in the organizational chart. The two reports are
guaranteed to be distinct.
Write a function that returns the lowest common manager to the two reports.
Sample Input:
// From the organizational chart below.
topManager = Node A
reportOne = Node E
reportTwo = Node I
          A
       /     \
      B       C
    /   \   /   \
   D     E F     G
 /   \
H     I

Sample Output:
Node B

Hints:
1. Given a random subtree in the organizational chart, the manager at the root of that subtree is common to any two
reports in the subtree.
2. Knowing Hint #1, the lowest common manager to two reports in an organizational chart is the root of the lowest subtree
containing those two reports. Find that lowest subtree to find the lowest common manager.
3. To find the lowest subtree containing both of the input reports, try recursively traversing the organizational chart
and keeping track of the number of those reports contained in each subtree as well as the lowest common manager in each
subtree. Some subtrees might contain neither of the two reports, some might contain one of them, and others might contain
both; the first to contain both should return the lowest common manager for all the subtrees above it that contain it,
including the entire organizational chart.

Optimal Space & Time Complexity
O(n) time | O(d) space - where n is the number of people in the org and d is the depth (height) of the org chart

https://github.com/lee-hen/Algoexpert/tree/master/hard/29_lowest_common_manager#hints
"""


class OrgChart:
    def __int__(self, name):
        self.name = name
        self.direct_reports = []


class Info:
    def __init__(self, lcm, reports):
        self.lowest_common_manager = lcm
        self.reports_found = reports


def get_lowest_common_manager(top_manager, report_one, report_two):
    return find_lowest_common_manager(top_manager, report_one, report_two).lower_common_manager


def find_lowest_common_manager(manager, report_one, report_two):
    reports_found = 0
    for report in manager.direct_reports:
        info = find_lowest_common_manager(report, report_one, report_two)
        if info.lowest_common_manager is not None:
            return info
        reports_found += info.reports_found
    if manager == report_one or manager == report_two:
        reports_found += 1
    lowest_common_manager = manager if reports_found == 2 else None
    return Info(lowest_common_manager, reports_found)


def main():
    pass


if __name__ == "__main__":
    main()


