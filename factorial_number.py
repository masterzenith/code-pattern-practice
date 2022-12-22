def factorial_number(num):
    factorial = 1
    if num < 0:
        print("Factorial does not exist for negative numbers")
    elif num == 0 or num == 1:
        print("The factorial of 0 or 1 is 1")
    else:
        for i in range(2, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)


factorial_number(3)
