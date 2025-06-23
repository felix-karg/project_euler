"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 == 17.
Find the sum of all the primes below two millions.
"""


limit = 2_000_000
sum = 0

def is_prime_number(a):
    if a <= 1:
        return False
    if a <= 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False

    i = 5
    while i * i <= a:
        if a % i == 0 or a % (i + 2) == 0:
            return False
        i += 6
    return True


for x in range(1, limit):
    if is_prime_number(x):
        sum += x

print(sum)
