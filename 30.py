"""Question: 30
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even,
otherwise print "It is an odd number"""


def checkParity(arg1):
    if arg1 % 2 == 0:
        print(str(arg1) + " It is an even number")
    else:
        print(str(arg1) + " It is an odd number")
