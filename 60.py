"""Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

data = input("Pleas insert a natural number bigger than 0: ")
result = 0
for i in range(1, int(data) + 1):
    result += i / (i + 1)
print("{:2f}".format(float(result)))
