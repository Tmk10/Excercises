"""Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
"""


def farmsolver(heads: "int number of heads", legs: "int number of legs") -> print():
    for x in range(heads + 1):
        y = heads - x
        if x * 4 + y * 2 == legs:
            print(" There are {} rabbits and {} chickens on the farm.".format(x, y))
            break
    else:
        print("No solution")


farmsolver(35, 100)
