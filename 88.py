"""With a given list [12,24,35,24,88,120,155,88,120,155],
write a program to print this list after removing all duplicate values with original order reserved."""

data = [12, 24, 35, 24, 88, 120, 166, 155, 88, 166, 120, 155]
newli = []
for x in data:
    if x in newli:
        continue
    else:
        newli.append(x)

print(newli)
