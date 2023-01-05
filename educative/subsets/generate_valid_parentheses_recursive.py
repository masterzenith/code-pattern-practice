"""

"""


def generate_valid_parentheses_recursive(num):
    result = []
    parentheses_string = [0 for x in range(2 * num)]
    generate_valid_parentheses_helper(num, 0, 0, parentheses_string, 0, result)
    return ''.join(result)


def generate_valid_parentheses_helper(num, open_count, close_count, parentheses_string, index, result):
    # if we reach the max number of open and close parentheses, add to the result
    if open_count == num and close_count == num:
        result.append(''.join(parentheses_string))
    else:
        if open_count < num:    # if we can add an open parentheses, add it
            parentheses_string[index] = '('
            generate_valid_parentheses_helper(num, open_count + 1, close_count, parentheses_string, index + 1, result)

        if open_count > close_count:    # if we can add a close parentheses, add it
            parentheses_string[index] = ')'
            generate_valid_parentheses_helper(num, open_count, close_count + 1, parentheses_string, index + 1, result)


def main():
    print("All combinations of balanced parentheses are: " + str(generate_valid_parentheses_recursive(2)))
    print("All combinations of balanced parentheses are: " + str(generate_valid_parentheses_recursive(3)))


if __name__ == "__main__":
    main()
