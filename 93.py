"""Question: 93

Please write a program which prints all permutations of [1,2,3]


Hints:
Use itertools.permutations() to get permutations of list.

"""
"""Solution 1"""
import itertools

print(list(itertools.permutations([1, 2, 3])))

"""Solution 2"""
import random
import math

li = [1, 2, 3]
perm = math.factorial(len(li))
perli = [li[:], ]
i = 1
while i < perm:
    random.shuffle(li)
    if li in perli:
        continue
    else:
        perli.append(li[:])
        i += 1
print(perli)
