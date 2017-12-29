"""Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield"""

def sevenGenerator(number):

    for i in range(1,number):
        if i % 7 == 0:
            yield i