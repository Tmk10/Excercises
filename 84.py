"""By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
Hints:
Use list comprehension to make an array."""

array3d = [[[0 for x in range(3)] for i in range(5)] for j in range(8)]

print(array3d)
