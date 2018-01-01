"""Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions."""

def zeroDivision():

    return 5/0

try:
    zeroDivision()
except ZeroDivisionError:
    print("Próba dzielenia przez 0")

