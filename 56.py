"""Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print
the user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input."""

"""Solution 1
print("Enter e-mail address: ")
data = input().split("@")
print(data[0])
"""

"""Solution 2"""
import re

print("Enter e-mail address: ")
data = input()
name = re.match('(\w+)(@)(\w+)\.(\w+)', data)

print("Name from e-mail: " + name.group(1))
print("Email without domain: " + name.group(1) + name.group(2) + name.group(3))
