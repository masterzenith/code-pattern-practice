def odd_numbers():
    count_odd = 0
    count_even = 0
    for x in (0, 60):
        if x % 2:
            count_even += 1
        else:
            count_odd += 1
    print("Number of even numbers :", count_even)
    print("Number of odd numbers :", count_odd)

print(odd_numbers())