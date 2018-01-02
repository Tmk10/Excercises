"""Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints:
Use yield to produce the next value in generator.
"""

n = input("Input a number fo generator")
a = (x for x in range(0, int(n) + 1) if x % 2 == 0)
print(type(a))
print(",".join(map(str, list(a))))
