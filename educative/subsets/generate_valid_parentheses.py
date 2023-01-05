"""
For a given number 'N', write a function to generate all combination of 'N' pairs of balanced parentheses.
I/P: N= 2
O/P: (()), ()()

I/P: N=3
O/P: ((())), (()()), (())(), ()()()

Time: O(N*2^N)
Space: O(N*2^N)
"""
from collections import deque


class ParenthesesString:
    def __init__(self, str, open_count, close_count):
        self.str = str
        self.open_count = open_count
        self.close_count = close_count


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        ps = queue.popleft()
        # If we've reached the maximum number of open and close parentheses, add to the result
        if ps.open_count == num and ps.close_count == num:
            result.append(ps.str)
        else:
            if ps.open_count < num:     # if we can add an open parentheses, add it
                queue.append(ParenthesesString(ps.str + "(", ps.open_count + 1, ps.close_count))
            if ps.open_count > ps.close_count:    # if we can add a close parentheses, add it
                queue.append(ParenthesesString(ps.str + ")", ps.open_count, ps.close_count + 1))
    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))

    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


if __name__ == "__main__":
    main()
