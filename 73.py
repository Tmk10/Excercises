"""Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive."""

import random

a = []
while len(a) < 5:
    a.append(round(random.uniform(100, 201), 2))
print(a)

""" Solution 2"""

b = random.sample(range(100, 201), 5)
print(b)