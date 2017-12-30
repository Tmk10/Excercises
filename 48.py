"""Question: 47
Define a class named American which has a static method called printNationality."""

class American:

    def printNationality():
        print("Static method which can be called from Class")
    printNationality = staticmethod(printNationality)

joey = American()
joey = joey.printNationality()
American.printNationality()
