"""Question 24
Level 1

Question:
    Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function

Hints:
"""

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def func(a : int) -> int:
    """This function does nothing except printing some info using builtin __doc__ function"""


print(func.__doc__)

