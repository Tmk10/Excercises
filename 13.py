"""Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

digits=0
letters=0
data = input("Write down a sentence")
for sign in data:
    if sign.isalpha():
        letters +=1
    if sign.isdigit():
        digits +=1
print("LETTERS " + str(letters) + "\n" + "DIGITS " + str(digits))
