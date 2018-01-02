"""Please write a program to output a random number, which is divisible by 5 and 7,
between 0 and 200 inclusive using random module and list comprehension."""

import random

a = random.choice([x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0])
print(a)
