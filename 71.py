"""Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension."""
import random

a = random.choice([x for x in range(0, 11) if not x % 2])
print(a)