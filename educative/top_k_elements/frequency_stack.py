"""
Frequency Stack:
Design a class that simulates a Stack data structure, implementing the following two operations:
1. push(int num): Pushes the number 'num' on the stack.
2. pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.

Example:
After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)
1. pop() should return 2, as it is the most frequent number
2. Next pop() should return 1
3. Next pop() should return 2

Time: The time complexity of push() and pop() is O(logN) where 'N' is the current number of elements in the heap.
Space: We will need O(N) space for the heap and the map, so the overall space complexity of the algorithm is O(N).
"""
from heapq import *


class Element:
    def __init__(self, number, frequency, sequence_number):
        self.number = number
        self.frequency = frequency
        self.sequence_number = sequence_number

    def __lt__(self, other):
        # higher frequency wins
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        # if both elements have same frequency, return the element that was pushed later
        return self.sequence_number > other.sequence_number


class FrequencyStack:
    sequence_number = 0
    max_heap = []
    frequency_map = {}

    def push(self, num):
        self.frequency_map[num] = self.frequency_map.get(num, 0) + 1
        heappush(self.max_heap, Element(num, self.frequency_map[num], self.sequence_number))
        self.sequence_number += 1

    def pop(self):
        num = heappop(self.max_heap).number
        # decrement the frequency or remove if this is the last number
        if self.frequency_map[num] > 1:
            self.frequency_map[num] -= 1
        else:
            del self.frequency_map[num]
        return num


def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


if __name__ == "__main__":
    main()
