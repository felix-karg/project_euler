# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

x = 1

def is_divisible(a):
    for b in range(1, 21):
        if a % b != 0:
            return False
    return True

while not is_divisible(x):
    x += 1

print(x)
