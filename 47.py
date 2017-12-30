"""Question: 46
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included)."""

result = list(map(lambda x: x ** 2, [i for i in range(1, 21)]))
print(result)
