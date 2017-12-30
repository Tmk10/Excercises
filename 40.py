"""Question: 40
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values
in one line and the last half values in one line."""

values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(str(values[:int(len(values) / 2)]) + "\n" + str(values[int(len(values) / 2):]))
