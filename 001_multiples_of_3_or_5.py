limit = 1000
multiples = []

for x in range(limit):
    if x % 3 == 0 or x % 5 == 0:
        multiples.append(x)

sum = 0

for multiple in multiples:
    sum += multiple

print(sum)