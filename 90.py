"""
Please write a program which count and print the numbers of each character in a string input by console.
Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1
Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value."""

data = input("Enter a string: ")
result = {}
for x in data:
    if result.get(x) != None:
        result[x] += 1
    else:
        result[x] = 1

print("\n".join((["{0} , {1}".format(x,y) for x,y in result.items()])))
