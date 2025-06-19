# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?


limit = 10_001
z = 2
counter = 1

def is_prime(x):
    for y in range(2, x):
        if x % y == 0:
            return False
    return True

while counter < limit:
    z += 1
    if is_prime(z):
        counter += 1

print(z)