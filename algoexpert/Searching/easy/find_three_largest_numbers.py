"""
Find Three Largest Numbers
Write a function that takes in an array of at least three integers and, without sorting the input array, returns a sorted
array of the three largest integers in the input array.
The function should return duplicate integers if necessary; for example, it should return [10, 10, 12] for an input array
of [10, 5, 9, 10, 12].

Sample Input:
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample Output:
[18, 141, 541]

Hints:
1. Can you keep track of the three largest numbers in an array as you traverse the input array?
2. Following the suggestion in Hint #1, try traversing the input array and updating the three largest numbers if necessary
by shifting them accordingly.

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the input array

Another Solution:
https://github.com/das-jishu/algoexpert-data-structures-algorithms/blob/master/Easy/find-three-largest-numbers.py
"""


def find_three_largest_numbers(array):
    largest_numbers = [None, None, None]
    for elem in array:
        # print(largest_numbers)
        check_and_update(array, elem, largest_numbers)
    return largest_numbers


def check_and_update(array, num, largest_numbers):
    if largest_numbers[2] is None or num > largest_numbers[2]:
        update_result(largest_numbers, num, 2)
    elif not largest_numbers[1] or num > largest_numbers[1]:
        update_result(largest_numbers, num, 1)
    elif not largest_numbers[0] or num > largest_numbers[0]:
        update_result(largest_numbers, num, 0)
    else:
        pass


def update_result(largest_numbers, num, index):
    # print("Update result")
    for i in range(index + 1):
        if i == index:
            largest_numbers[i] = num
        else:
            largest_numbers[i] = largest_numbers[i + 1]


def main():
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    print(find_three_largest_numbers(array))


if __name__ == "__main__":
    main()
