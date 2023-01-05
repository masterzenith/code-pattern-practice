"""
Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be
evaluated by grouping the numbers and operators using parentheses.
I/P: "1+2*3"
O/P: 7, 9
Explanation: 1+(2*3) => 7 and (1+2)*3 => 9

Time: O(N*2^N)
Space: O(N*2^N)
"""


def diff_ways_to_evaluate_expression(input):
    result = []
    # base case: if the input string is a number, parse and add it to output
    if '+' not in input and '-' not in input and '*' not in input:
        result.append(int(input))
    else:
        for i in range(0, len(input)):
            char = input[i]
            if not char.isdigit():
                # break the equation here into two parts and make recursively calls
                left_parts = diff_ways_to_evaluate_expression(input[0:i])
                right_parts = diff_ways_to_evaluate_expression(input[i + 1:])
                for part1 in left_parts:
                    for part2 in right_parts:
                        if char == '+':
                            result.append(part1 + part2)
                        elif char == '-':
                            result.append(part1 - part2)
                        elif char == '*':
                            result.append(part1 * part2)
    return result


def main():
    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("1+2*3")))
    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("2*3-4-5")))


if __name__ == "__main__":
    main()
