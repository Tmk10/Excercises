"""
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

Hints:
Use set() and "&=" to do set intersection operation.
"""

data1 = [1,3,6,78,35,55]
data2 = [12,24,35,24,88,120,155]
data3 = list(set(data1) & set(data2))
print(data3)