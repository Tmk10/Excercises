"""Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
"""

heads = 35
legs = 94
animals = 0
rabbits = 0
chickens = 0

for rabbit in range(0, heads):
    animals += 1
    rabbits += 1
    heads -= 1
    legs -= 4
    if legs / 2 == heads and animals + heads == 35:
        legs -= heads *2
        chickens = heads
        break

print("There are {} rabbits and {} chickens on the farm  {}".format(rabbits, chickens,legs))


