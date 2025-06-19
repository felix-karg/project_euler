# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 == 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 == 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 == 2640
# Find the difference between the sum of the squares of the first one hundret natural numbers and the square ot the sum.

limit = 100

def sum_of_squares(x):
    sum = 0
    for y in range(1, x + 1):
        sum += y**2
    return sum

def square_of_the_sum(x):
    sum = 0
    for y in range(1, x + 1):
        sum += y
    return sum**2

print(square_of_the_sum(limit) - sum_of_squares(limit))