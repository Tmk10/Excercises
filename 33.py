"""Question: 33
Define a function which can generate a dictionary where the keys are numbers between 1 and 20
(both included) and the values are square of keys. The function should just print the values only."""


def printdictvalues():
    result = {x: x ** 2 for x in range(1, 21)}
    values = [str(result.get(x)) for x in result]
    print(",".join(values))
