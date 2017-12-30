"""Question: 34
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys. The function should just print the keys only."""


def printdictkeys():
    result = {x: x ** 2 for x in range(1, 21)}
    keys = list(result.keys())
    keys = map(str, keys)
    print(",".join(keys))


printdictkeys()
