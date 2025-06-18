"""
A palindromic number reads the same both  ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(a):
    a_str = str(a)
    for b in range(len(a_str) // 2):
        if a_str[b] != a_str[-(b + 1)]:
            return False
    return True
    

palindromes = []

for x in range (100, 1000):
    for y in range(100, 1000):
        if is_palindrome(x * y):
            palindromes.append(x * y)

print(max(palindromes))
