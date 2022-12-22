def change(amount):

    # this can be removed if you pass the amount in pennies
    # rather than dollars
    amount = int(round(amount*100))

    values = [2000, 1000, 500, 100, 25, 10, 5, 1]
    denom = ['twenties', 'tens', 'fives', 'ones', 'quarters', 'dimes', 'nickels', 'pennies']

    for i in range(len(values)):
        num = amount / values[i]
        amount -= num * values[i]
        print(str(num) + " " + denom[i])
print(change(58.79))