"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 == c**2.
For example, 3**2 + 4**2 == 9 + 16 == 25 == 5**2.
There exists exactly one Pythagorean triplet for which a + b + c == 1000.
Find the product a * b * c.
"""

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        for c in range(b + 1, 1000):
            if (a + b + c == 1000):
                if (a**2 + b**2 == c**2):
                    print(a * b * c)
                    exit()
