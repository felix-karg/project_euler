"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


test_number = 600_851_475_143
prime_factors = []

def is_prime_number(a):
    for b in range(2, a):
        if a % b == 0:
            return False
    return True

while test_number > 1:
    for x in range(2, test_number + 1):
        if test_number % x == 0:
            if is_prime_number(x):
                prime_factors.append(x)
                test_number //= x
                break

print(max(prime_factors))
