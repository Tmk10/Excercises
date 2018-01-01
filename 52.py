"""Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default."""


class Shape:
    def __init__(self):
        pass
    def computeArea(self):
       return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def computeArea(self):
        return self.length * self.length

shape1 = Shape()
square1 = Square(3)
print(shape1.computeArea())
print(square1.computeArea())