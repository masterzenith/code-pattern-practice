"""
Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to
put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but you can't skip a tree once you have started. You will pick one fruit from each tree
until you cannot, you will stop when you have to pick from a third fruit type.
Write function to return the maximum number of fruits in both the baskets.

I/P: Fruit=['A', 'B', 'C', 'A', 'C']
O/P: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

I/P: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
O/P: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

Time: The time complexity of the algorithm will be O(N)
Space: The algorithm runs in constant space O(1) as there can be a maximum of three types of fruits stored in the frequency
map

Similar Problem:
Given a string, find the length of the longest substring in it with at most two distinct characters.
Solution: Similar to above
"""


def fruits_into_baskets(fruits):
    window_start = 0
    max_length = 0
    fruit_frequency = {}

    # try to extend the range [window_start, window_end]
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1   # shrink the window
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


if __name__ == "__main__":
    main()
