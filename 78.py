"""Question: 78

Please write a program to print the running time of execution of "1+1" for 100 times.
"""


import timeit

a = timeit.Timer("for i in range (0,100): 1+1")
print(a.timeit())