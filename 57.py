"""Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
"""

import re

print("Enter e-mail address: ")
data = input()
name = re.match('(\w+)(@)(\w+)\.(\w+)', data)

print("E-mail address domain: " + name.group(3))
