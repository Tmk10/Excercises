"""Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""

print("Insert  transactions: ")
balance={"D" : 0,"W" :0}
while True:
    data = input()
    if data:
        data = data.split(" ")
        if data[0] == "D":
            balance["D"] += int(data[1])
        if data[0] == "W":
            balance["W"] += int(data[1])
    else:
        break

result = balance["D"] - balance["W"]
print("The balance is: " + str(result))




