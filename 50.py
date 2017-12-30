"""uestion: 50
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area."""


class Circle:


    def __init__(self, radius):
        self.radius = radius

    def computeArea(self):
        import math
        return math.pi * self.radius ** 2

circle1 = Circle(5)
circle2 = Circle(10)

print(circle1.computeArea())
print(circle2.computeArea())
