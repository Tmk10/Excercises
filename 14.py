"""Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""

upper=0
lower=0
data = input("Write down a sentence")
for sign in data:
    if sign.islower():
        lower +=1
    if sign.isupper():
        upper +=1
print("UPPER CASE {0}   \nLOWER CASE {1}".format(upper,lower))