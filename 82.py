"""
Question: 82

By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.

"""
data = [12, 24, 35, 70, 88, 120, 155]
data = [x for x in data if x % 5 and x % 7]
print(data)

