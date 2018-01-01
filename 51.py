"""7.2 Question: 51

Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def computeArea(self):
        return self.length * self.width


rectangle1 = Rectangle(10, 20)
rectangle2 = Rectangle(30, 50)
print(rectangle1.computeArea())
print(rectangle2.computeArea())
