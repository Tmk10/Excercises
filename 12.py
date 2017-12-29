"""Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""

result=[]
for x in range(2000,3001):
    count = 0
    for i in str(x):
        if int(i) % 2 == 0:
            count += 1
    if count == 4:
        result.append(str(x))


print(", ".join(result))

