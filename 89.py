"""
Define a class Person and its two child classes: Male and Female.
All classes have a method "getGender" which can print "Male"
 for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.
"""


class Person:
    gender = None
    def getGender(self):
        print(self.gender)


class Male(Person):

    def __init__(self):
        self.gender = "Male"


class Female(Person):

    def __init__(self):
        self.gender = "Female"



john = Male()
john.getGender()
jane = Female()
jane.getGender()
Male.gender = None
john.getGender()




