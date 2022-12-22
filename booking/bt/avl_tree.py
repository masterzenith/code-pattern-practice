import math
from collections import deque


def minimumSumAfterOperations(arr, k):
    sum = 0
    length = len(arr)

    queue = deque()
    for i in range(0, length - 1):
        queue.append(arr[i])

        while queue and k > 0:
            maxElement = queue.pop()

            queue.append(math.ceil(maxElement / 2))
            k -= 1

        for number in queue:
            print(number)
            sum += number
        return sum


minimumSumAfterOperations([10, 20, 7], 4)
