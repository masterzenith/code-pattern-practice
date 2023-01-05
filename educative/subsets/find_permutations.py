"""
Given a set of distinct numbers, find all of its permutations.
Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following
six permutations:
1. {1, 2, 3}
2. {1, 3, 2}
3. {2, 1, 3}
4. {2, 3, 1}
5. {3, 1, 2}
6. {3, 2, 1}
If a set has 'n' distinct elements it will have n! permutations.
Example 1:
I/P: [1, 3, 5]
O/P: [1, 3, 5], [1, 5, 3], [3, 1, 5], [3, 5, 1], [5, 1, 3], [5, 3, 1]

Time: O(N*N!)
Space: O(N*N!)
"""
from collections import deque


def find_permutations(nums):
    nums_length = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for current_number in nums:
        # we will take all existing permutations and add the current number to create new permutations
        n = len(permutations)
        for _ in range(n):
            old_permutation = permutations.popleft()
            # create a new permutation by adding the current number at every position
            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, current_number)
                if len(new_permutation) == nums_length:
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)
    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


if __name__ == "__main__":
    main()
