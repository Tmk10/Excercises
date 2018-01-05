"""By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple."""

data = [12, 24, 35, 70, 88, 120, 155]
data = [y for (x, y) in enumerate(data) if x != 0 and x != 4 and x != 5]

print(data)
