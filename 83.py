"""uestion: 83

By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints:

Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple."""

data = [12, 24, 35, 70, 88, 120, 155]

data = [x[1] for x in enumerate(data) if x[0] % 2 ]

print(data)