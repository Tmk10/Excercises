"""Question: 42
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". """
import re

data = input("Input text: ")
if re.search(r'\bYes\b|\byes\b|\bYES\b', data):
    print("Yes")
else:
    print("No")
