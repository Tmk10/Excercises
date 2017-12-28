"""Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters"""

class NewString:
    def __init__(self, value):
        self.value = value
    def getString(self):
        self.value = input("Please insert a word: ")
    def printString(self):
        self.value = self.value.upper()
        print(self.value)
a = NewString("Example")
a.printString()
a.getString()
a.printString()