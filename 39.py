"""Question: 39
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included)."""


def squarelist():
    squares = tuple([str(x ** 2) for x in range(1, 21)])
    print(",".join(squares))


squarelist()
