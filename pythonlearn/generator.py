# # # A simple generator function
# # def my_gen():
# #     n = 1
# #     print('This is printed first')
# #     # Generator function contains yield statements
# #     yield n
# #
# #     n += 1
# #     print('This is printed second')
# #     yield n
# #
# #     n += 1
# #     print('This is printed at last')
# #     yield n
# #
# # # Using for loop
# # for item in my_gen():
# #     print(item)
#
# # def rev_str(my_str):
# #     length = len(my_str)
# #     for i in range(length - 1, -1, -1):
# #         yield my_str[i]
# #
# #
# # # For loop to reverse the string
# # for char in rev_str("hello"):
# #     print(char)
#
# # Initialize the list
# my_list = [1, 3, 6, 10]
#
# # square each term using list comprehension
# list_ = [x**2 for x in my_list]
# generator = (x**2 for x in my_list)
#
# print(list_)
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(sum(x**2 for x in my_list))
# print(max(x**2 for x in my_list))

# class PowTwo:
#     def __init__(self, max=0):
#         self.n = 0
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n > self.max:
#             raise StopIteration
#         result = 2 ** self.n
#         self.n += 1
#         return result
# def PowTwoGen(max=0):
#     n = 0
#     while n < max:
#         yield 2 ** n
#         n += 1
# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


print(sum(square(fibonacci_numbers(10))))
