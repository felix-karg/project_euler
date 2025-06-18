"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


limit = 1000
multiples = []

for x in range(limit):
    if x % 3 == 0 or x % 5 == 0:
        multiples.append(x)

sum = 0

for multiple in multiples:
    sum += multiple

print(sum)
