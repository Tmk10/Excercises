"""Question 21
Level 3

Question£º
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""
import math

print("Enter robot moves: ")
movement = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}
while True:
    data = input()
    if data:
        data = data.split(" ")
        if data[0] == "UP":
            movement["UP"] = int(data[1])
        if data[0] == "DOWN":
            movement["DOWN"] = int(data[1])
        if data[0] == "LEFT":
            movement["LEFT"] = int(data[1])
        if data[0] == "RIGHT":
            movement["RIGHT"] = int(data[1])
    else:
        break
print("Robot moves: \n" + str(movement))
a = movement["UP"] - movement["DOWN"]
b = movement["LEFT"] - movement["RIGHT"]
result = round(math.sqrt(a ^ 2 + b ^ 2))
print(result)
