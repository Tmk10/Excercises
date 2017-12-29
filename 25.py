"""Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
"""


class Cls:
    classAtribute = "Atrybut klasy"

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

print(Cls.__name__)
print(Cls.classAtribute)
instancja = Cls("Nowa instancja")
print(instancja)

